# first line: 217
def plot_segmentation(img, gm_filename, wm_filename=None,
                      csf_filename=None,
                      output_filename=None, cut_coords=None,
                      display_mode='ortho',
                      cmap=None,
                      title='GM + WM + CSF segmentation'):
    """
    Plot a contour mapping of the GM, WM, and CSF of a subject's anatomical.

    Parameters
    ----------
    img_filename: string or image object
                  path of file containing image data, or image object simply

    gm_filename: string
                 path of file containing Grey Matter template

    wm_filename: string (optional)
                 path of file containing White Matter template

    csf_filename: string (optional)
                 path of file containing Cerebro-Spinal Fluid template


    """
    # misc
    if cmap is None:
        cmap = pl.cm.gray
    if cut_coords is None:
        cut_coords = (-10, -28, 17)
    if display_mode in ['x', 'y', 'z']:
        cut_coords = (cut_coords['xyz'.index(display_mode)],)

    # plot img
    img = mean_img(img)
    img = reorder_img(img, resample="continuous")
    _slicer = plot_img(img, cut_coords=cut_coords, display_mode=display_mode,
                       cmap=cmap, black_bg=True)

    # add TPM contours
    gm = nibabel.load(gm_filename)
    _slicer.add_contours(gm, levels=[.51], colors=["r"])
    if not wm_filename is None:
        _slicer.add_contours(wm_filename, levels=[.51], colors=["g"])
    if not csf_filename is None:
        _slicer.add_contours(csf_filename, levels=[.51], colors=['b'])

    # misc
    _slicer.title("%s (cmap: %s)" % (title, cmap.name), size=12, color='w',
                 alpha=0)
    if not output_filename is None:
        pl.savefig(output_filename, bbox_inches='tight', dpi=200,
                   facecolor="k",
                   edgecolor="k")
        pl.close()
