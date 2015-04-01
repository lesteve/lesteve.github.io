# first line: 145
def plot_registration(reference_img, coregistered_img,
                      title="untitled coregistration!",
                      cut_coords=None,
                      display_mode='ortho',
                      cmap=None,
                      output_filename=None):
    """Plots a coregistered source as bg/contrast for the reference image

    Parameters
    ----------
    reference_img: string
        path to reference (background) image

    coregistered_img: string
        path to other image (to be compared with reference)

    display_mode: string (optional, defaults to 'ortho')
        display_mode param to pass to the nipy.labs.viz.plot_??? APIs

    cmap: matplotlib colormap object (optional, defaults to spectral)
        colormap to user for plots

    output_filename: string (optional)
        path where plot will be stored

    """

    # sanity
    if cmap is None:
        cmap = pl.cm.gray  # registration QA always gray cmap!

    if cut_coords is None:
        cut_coords = (-10, -28, 17)

    if display_mode in ['x', 'y', 'z']:
        cut_coords = (cut_coords['xyz'.index(display_mode)],)

    # plot the coregistered image
    if hasattr(coregistered_img, '__len__'):
        coregistered_img = load_specific_vol(coregistered_img, 0)[0]

    # XXX nilearn complains about rotations in affine, etc.
    coregistered_img = reorder_img(coregistered_img, resample="continuous")

    _slicer = plot_img(coregistered_img, cmap=cmap, cut_coords=cut_coords,
              display_mode=display_mode, black_bg=True)

    # overlap the reference image
    if hasattr(reference_img, '__len__'):
        reference_img = load_specific_vol(reference_img, 0)[0]

    # XXX nilearn complains about rotations in affine, etc.
    reference_img = reorder_img(reference_img, resample="continuous")

    _slicer.add_edges(reference_img)

    # misc
    _slicer.title("%s (cmap: %s)" % (title, cmap.name), size=12, color='w',
                  alpha=0)

    if not output_filename is None:
        try:
            pl.savefig(output_filename, dpi=200, bbox_inches='tight',
                       facecolor="k",
                       edgecolor="k"
                       )
            pl.close()
        except AttributeError:
            # XXX TODO: handle this case!!
            pass
