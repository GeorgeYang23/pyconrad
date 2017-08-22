# pyConrad



A python wrapper for the CONRAD framework (https://www5.cs.fau.de/conrad/)


# CONRAD


CONRAD is a state-of-the-art software platform with extensive documentation. It is based on platform-independent technologies. Special libraries offer access to hardware acceleration such as CUDA and OpenCL. There is an easy interface for parallel processing. The software package includes different simulation tools that are able to generate 4-D projection and volume data and respective vector motion fields. Well known reconstruction algorithms such as FBP, DBP, and ART are included. All algorithms in the package are referenced to a scientific source. Please visit http://conrad.stanford.edu for more information.

# Installation


Install via pip:

    pip install git+https://git5.cs.fau.de/PyConrad/pyconrad_java.git
    pip install pyconrad


This will automatically install CONRAD and all python dependencies. You can use the following python code to get the installation directory of CONRAD:
``` python
    import pyconrad_java
    print( pyconrad_java.conrad_jar_dir )
```

# Usage

You can start CONRAD like this:
``` python
    from pyconrad import PyConrad
    
    # PyConrad is a singleton class
    pyconrad = PyConrad()
    # setup PyConrad
    pyconrad.setup()
    # start CONRAD
    pyconrad.start_conrad()  # or pyconrad.start_reconstruction_filter_pipeline()
```

The central class of the pyconrad package is PyConrad. You can use it to access all Java classes of CONRAD and start the graphical user interface:
``` python
    from pyconrad import PyConrad
    
    pyconrad = PyConrad()
    pyconrad.setup()
    # Optional parameters for Java Virtual Machine RAM and own Java projects
    # pyconrad.setup(max_ram = '8G', min_ram= '500M', dev_dirs=['path/to/project/with/own/java/classes']
    
    # Create Phantom (edu.stanford.rsl.tutorial.phantoms.MickeyMouseGrid2D)
    phantom = pyconrad.classes.stanford.rsl.tutorial.phantoms.MickeyMouseGrid2D(300, 300)
    # Some packages can be accessed more easily
    phantom2 = pyconrad.get_phantom_package().MickeyMouseGrid2D(200,200)
    
    # Use Java method of class MickeyMouseGrid2D
    phantom.show()
```
To transfer data from NumPy to Conrad use the class PyGrid:
```python
    from pyconrad import PyConrad, PyGrid, java_float_dtype
    import numpy as np
    
    pyconrad = PyConrad()
    pyconrad.setup()
    
    phantom = pyconrad.get_phantom_package().MickeyMouseGrid2D(200,200)
    
    # Create PyGrid from Grid2D
    pygrid1 = PyGrid.from_grid(phantom)
    # use Java method
    pygrid1.grid().show()
    # use Python method
    from scipy.misc import imshow
    imshow(pygrid1.numpy()) # or imshow(pygrid1)
```
Data changes have to be synchronized:
``` python
    ...

    # Create PyGrid from numpy array (must be of type pyconrad.java_float_dtype)
    array = np.random.rand(4,2,3).astype(java_float_dtype)
    pygrid2 = PyGrid.from_numpy(array)

    # Manipulate data in using CONRAD at Position (x,y,z) = (1,2,4)
    pygrid2.grid().setValue(5.0, [0,1,3])
    
    # Print this pixel using Python indexes [z,y,x]
    print("Before update: %f" % pygrid2[3,1,0])
    # Python data must be synchronized with CONRAD
    pygrid2.update_numpy()
    print("After update: %f" % pygrid2[3,1,0])
    
    # Manipulate pixel using python
    pygrid2[1,1,1] = 3.0
    # Update CONRAD data
    pygrid2.update_grid()
    
    # Print
    print(pygrid2)    

```

More examples can found [here](examples)