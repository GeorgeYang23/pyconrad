
# Copyright (C) 2010-2017 - Andreas Maier
# CONRAD is developed as an Open Source project under the GNU General Public License (GPL-3.0)

import pyconrad
import numpy as np

def _extend_pointnd():
    @classmethod
    def _pointnd_from_numpy(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble)(array.tolist()))

    @classmethod
    def _pointnd_from_list(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble)(array))

    def _numpy_pointnd(self):
        return np.array(self.getCoordinates()[:])

    pointnd_class = pyconrad.PyConrad().classes.stanford.rsl.conrad.geometry.shapes.simple.PointND
    pointnd_class.as_numpy = _numpy_pointnd
    pointnd_class.from_numpy = _pointnd_from_numpy
    pointnd_class.from_list = _pointnd_from_list

def _extend_simple_vector():
    @classmethod
    def _simple_vector_from_numpy(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble)(array.tolist()))

    @classmethod
    def _simple_vector_from_list(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble)(array))

    def _numpy_simple_vector(self):
        return np.array(self.copyAsDoubleArray())

    simple_vector_class = pyconrad.PyConrad().classes.stanford.rsl.conrad.numerics.SimpleVector
    simple_vector_class.as_numpy = _numpy_simple_vector
    simple_vector_class.from_numpy = _simple_vector_from_numpy
    simple_vector_class.from_list = _simple_vector_from_list

def _extend_simple_matrix():
    @classmethod
    def _simple_matrix_from_numpy(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble,np.ndim(array))(array.tolist()))

    @classmethod
    def _simple_matrix_from_list(cls, array):
        return cls(pyconrad.JArray(pyconrad.JDouble, np.ndim(array))(array))

    def _numpy_simple_matrix(self):
        return np.matrix(self.copyAsDoubleArray())

    simple_matrix_class = pyconrad.PyConrad().classes.stanford.rsl.conrad.numerics.SimpleMatrix
    simple_matrix_class.as_numpy = _numpy_simple_matrix
    simple_matrix_class.from_numpy = _simple_matrix_from_numpy
    simple_matrix_class.from_list = _simple_matrix_from_list

def _extend_numeric_grid():

    @classmethod
    def _numeric_grid_from_numpy(cls,array):
        if array.dtype == pyconrad.java_float_dtype:
            return pyconrad.PyGrid.from_numpy(array).grid()
        else:
            return pyconrad.PyGrid.from_numpy(np.array(array,pyconrad.java_float_dtype)).grid()

    @classmethod
    def _numeric_grid_from_list(cls,input_list):
        return pyconrad.PyGrid.from_numpy(np.array(input_list,pyconrad.java_float_dtype)).grid()

    def _numpy_grid(self):
        return np.array(pyconrad.PyGrid.from_grid(self))

    def _numeric_grid_getitem(self, idxs):
        if isinstance(idxs, int) and not isinstance(self, pyconrad.PyConrad().classes.stanford.rsl.conrad.data.numeric.Grid1D):
            return self.getSubGrid(idxs)
        elif isinstance(idxs, slice) and isinstance(self, pyconrad.PyConrad().classes.stanford.rsl.conrad.data.numeric.Grid3D):
            start = idxs.start or 0
            end = idxs.stop or self.getSize()[2]
            assert idxs.step == 1 or not idxs.step, "Only step==1 is supported"

            rtn = pyconrad.PyConrad().classes.stanford.rsl.conrad.data.numeric.Grid3D(self.getSize()[0],self.getSize()[1], end - start, False)
            for i in range(start, end):
                rtn.setSubGrid(i - start, self.getSubGrid(i))
            return rtn
        else:
            return self.getValue(idxs)

    def _numeric_grid_setitem(self, idxs, value):
        if isinstance(idxs, int) and not isinstance(self, pyconrad.PyConrad().classes.stanford.rsl.conrad.data.numeric.Grid1D):
            return self.setSubGrid(idxs, value)
        else:
            return self.setValue(idxs, value)

    @property
    def _numeric_grid_shape(self):
        return list(reversed(self.getSize()[:]))

    def _save_as_tiff(self, path):
        pyconrad.ImageUtil.save_grid_as_tiff(self, path)

    @staticmethod
    def _from_tiff(path):
        return pyconrad.ImageUtil.grid_from_tiff(path)

    grid_class = pyconrad.PyConrad().classes.stanford.rsl.conrad.data.numeric.NumericGrid
    grid_class.as_numpy = _numpy_grid
    grid_class.from_numpy = _numeric_grid_from_numpy
    grid_class.from_list = _numeric_grid_from_list
    grid_class.from_tiff = _from_tiff
    grid_class.save_tiff = _save_as_tiff
    grid_class.__getitem__ = _numeric_grid_getitem
    grid_class.__setitem__ = _numeric_grid_setitem
    grid_class.shape = _numeric_grid_shape

def extend_all_classes():
    _extend_pointnd()
    _extend_simple_vector()
    _extend_simple_matrix()
    _extend_numeric_grid()
