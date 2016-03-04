# VARCONVOLVE
A python module that performas a convolution with a kernel with a variable width. Any kernel can be used where width is a function of a single variable. 

Variability of the kernel width is achieved by warping the signal, performing the convolution with a fixed kernel and then unwarping the signal.

Only signals with uniform sampling can be convolved in the current version.

##Download

This software can be downloaded by cloning the git repository:

```bash
git clone https://github.com/sheliak/varconvolve.git
```

A folder `varconvolve` will be created

##Installation

A setup.py file is provided. The module can be installed in the usual way by running

```bash
cd varconvolve
sudo python setup.py install 
```
This will make the `varconvolve` module available system-wide.

##Usage

See `example.py` or keep reading.


###Define a kernel function
The module expects to have a kernel function available. Only one argument is required, the width of the kernel. What shape the kernel has or what the width actually means is irelevant. A minimal example here will produce a normalized boxy kernel:

```python
def kernel(w):
  w=int(w)
  return np.ones(w)/float(w)
```

The user must take care that the kernel is normalized, if this is required for his application. Width is given in natural units, not pixels.

###Define a width variability function
How the width of the kernel changes can be given in two different ways. The first one is to provide a function (like a linear function here):

```python
def var(x):
  return np.polyval([0.2,1],x)
```

The second way is to use an array of the same shape as the signal array where the width is sampled. Linear interpolation will be made to determine the kernel width between the sampled points.

###Run the convolution:
```python
y_convolved=varconvolve(x,y,kernel,var,oversample=1,mode='same')
```

The arguments are:
* `x` is the array with the sampling of the signal.
* `y` is the array with the signal.
* `kernel` is the name of the kernel function
* `var` is a function, a list or an array giving the kernel width.
* `oversample` is a float larger than 1 defining how much the signal will be oversampled in the process of making the convolution. 1 means no additional oversampling and a value greater than 1 means that that many points will be created for each point of the signal before the convolution is done. Use values greater than 1 only if accuracy is a big concern.
* `mode` is the mode of the returned convolved signal. See numpy's convolve for the explanation.

The returned parameters are:
* A convolved signal.

