#What is NumPy?
#NumPy is the fundamental package for scientific computing in Python. 
#It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices),
#and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, 
#sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

#from : https://numpy.org/doc/stable/user/whatisnumpy.html

### EXAMPLES from DC 
# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254,0.453592,1])

# Print out product of np_baseball and conversion
print(np_baseball*conversion)
