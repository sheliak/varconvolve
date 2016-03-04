import numpy as np
import scipy
from matplotlib.pyplot import *
import varconvolve as varcon

def kernel(s):
	"""
	Constructs a normalized discrete 1D gaussian kernel
	"""
	size_grid = int(s*4)
	x= scipy.mgrid[-size_grid:size_grid+1]
	g = scipy.exp(-(x**2/float(s**2)/2.))
	return g / np.sum(g)

def var(x):
	"""
	Creates a polynomial that describes the kernel width
	"""
	p=[0.2,0.02]
	return np.polyval(p,x)

#x sampling:
x=np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0])
#a delta function:
y=np.array([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
#a step function that describes the kernel width:
v=np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3])

plot(x,y,'k-')
y_c=varcon.varconvolve(x,y,kernel,var)
y_cc=varcon.varconvolve(x,y,kernel,v)
plot(x,y_c,'r-')
plot(x,y_cc,'b-')

show()