# author Bastian Bier

from jpype import  *
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

startJVM(getDefaultJVMPath(),
"-Djava.class.path=C:\\StanfordRepo\\pyConrad\\CONRAD 1.0.6\\conrad_1.0.6.jar", "-Xmx8G", "-Xmn7G") 
package = JPackage("edu").stanford.rsl.conrad.data.numeric
 
class ImageUtil:
    def wrapGrid2D(grid2D):
        w = grid2D.getWidth()
        h = grid2D.getHeight()
        array = np.asarray(grid2D.getBuffer())
        array = np.reshape(array, (h, w))
        return array
    
    def wrapGrid3D(grid3D):
        size = grid3D.getSize()
        array = np.zeros((size[1],size[0],size[2]))
        iter = 0
        for id in range(size[2]):
            for ih in range (size[1]):
                for iw in range (size[0]):
                    array[ih,iw,id] = grid3D.getAtIndex(iw,ih,id) 
                    iter = iter + 1
        array = np.reshape(array, (size[1],size[0],size[2]))
        return array
    
    def wrapNumpyArrayToGrid2D(array):
        dim = array.shape
        flattened = array.flatten()
        grid = package.Grid2D(flattened, dim[1], dim[0])
        return grid

    def wrapNumpyArrayToGrid3D(array):
        dim = array.shape
        grid = package.Grid3D(dim[1], dim[0], dim[2])
        for id in range(dim[2]):
            for ih in range (dim[1]):
                for iw in range (dim[0]):
                    grid.setAtIndex(ih,iw,id, array[iw,ih,id])
        return grid