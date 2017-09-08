
# Copyright (C) 2010-2017 - Andreas Maier
# CONRAD is developed as an Open Source project under the GNU General Public License (GPL-3.0)

from ._pyconrad import PyConrad
from ._pygrid import PyGrid

class ImageUtil:

    #################
    ## Save Images ##
    #################

    @staticmethod
    def save_grid_as_tiff(grid, path):
        PyConrad.get_instance().classes.stanford.rsl.conrad.utils.ImageUtil.saveAs(grid, path)

    @staticmethod
    def save_numpy_as_tiff(array, path):
        grid = ImageUtil.grid_from_numpy(array)
        PyConrad.get_instance().classes.stanford.rsl.conrad.utils.ImageUtil.saveAs(grid, path)

    #################
    ## Load Images ##
    #################

    @staticmethod
    def grid_from_tiff(path):
        ij = PyConrad.get_instance().ij.IJ.openImage(path)
        if not ij:
            raise RuntimeError('Error opening file \'%s\'' % path)
        grid = PyConrad.get_instance().classes.stanford.rsl.conrad.utils.ImageUtil.wrapImagePlus(ij)
        return grid

    @staticmethod
    def array_from_tiff(path):
        ij = PyConrad.get_instance().ij.IJ.openImage(path)
        if not ij:
            raise RuntimeError('Error opening file \'%s\'' % path)
        grid = PyConrad.get_instance().classes.stanford.rsl.conrad.utils.ImageUtil.wrapImagePlus()
        return ImageUtil.numpy_from_grid(grid)

