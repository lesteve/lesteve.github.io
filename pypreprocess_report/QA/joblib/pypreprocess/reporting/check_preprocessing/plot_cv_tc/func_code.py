# first line: 72
def plot_cv_tc(epi_imgs, session_ids, subject_id,
               do_plot=True, write_image=True, _output_dir=None,
               cv_tc_plot_outfile=None, **kwargs):
    """ Compute coefficient of variation of the data and plot it

    Parameters
    ----------
    epi_imgs: list of strings, input fMRI 4D images
    session_ids: list of strings of the same length as epi_imgs,
                 session indexes (for figures)
    subject_id: string, id of the subject (for figures)
    do_plot: bool, optional,
             should we plot the resulting time course
    write_image: bool, optional,
                 should we write the cv image
    mask: bool or string, optional,
          (string) path of a mask or (bool)  should we mask the data
    **kwargs:
        kwargs for plot_stat_map API
    """
    if _output_dir is None:
        if not cv_tc_plot_outfile is None:
            _output_dir = os.path.dirname(cv_tc_plot_outfile)
        else:
            _output_dir = tempfile.mkdtemp()

    cv_tc_ = []
    for (session_id, fmri_file) in zip(session_ids, epi_imgs):
        nim = load_4D_img(fmri_file)
        affine = nim.get_affine()
        if len(nim.shape) == 4:
            data = nim.get_data()
        else:
            raise TypeError("Expecting 4D image!")

        # compute the CV for the session
        cache_dir = os.path.join(_output_dir, "CV")
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        mem = joblib.Memory(cachedir=cache_dir, verbose=5)
        cv = nibabel.Nifti1Image(mem.cache(compute_cv)(data), affine)

        # XXX nilearn complains about rotations in affine, etc.
        cv = reorder_img(cv, resample="continuous")

        if write_image:
            # write an image
            cv.to_filename(os.path.join(_output_dir, 'cv_%s.nii' % session_id))
        plot_stat_map(cv, threshold=.01, **kwargs)

        # compute the time course of cv
        data = data.reshape((-1, data.shape[-1]))
        cv_tc_sess = np.median(np.sqrt((data.T / data.mean(axis=-1) - 1) ** 2),
                               axis=-1)
        cv_tc_.append(cv_tc_sess)
    cv_tc = np.concatenate(cv_tc_)

    # plot CV time-course
    if do_plot:
        pl.figure()
        pl.plot(cv_tc, label=subject_id)
        pl.legend()
        pl.xlabel('time(scans)')
        pl.ylabel('Median coefficient of variation')
        pl.axis('tight')
        if not cv_tc_plot_outfile is None:
            pl.savefig(cv_tc_plot_outfile,
                       bbox_inches="tight", dpi=200)
            pl.close()

    return cv_tc
