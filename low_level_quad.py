import numpy as np
from scipy import integrate
import ctypes

"""
Some functions in SciPy take as arguments callback functions, which can either be python callables or low-level compiled functions. Using compiled callback functions can improve performance somewhat by avoiding wrapping data in Python objects.

Such low-level functions in SciPy are wrapped in LowLevelCallable objects, which can be constructed from function pointers obtained from ctypes, cffi, Cython, or contained in Python PyCapsule objects.

LowLevelCallable

Low-level callback function.
"""


def x2(x): return x**2


print(integrate.quad(x2, 0, 4))
print(4**3 / 3.)


def invexp(x): return np.exp(-x)


print(integrate.quad(invexp, 0, np.inf))


def f(x, a): return a * x


y, err = integrate.quad(f, 0, 1, args=(1,))
print(y)
y, err = integrate.quad(f, 0, 1, args=(3,))
print(y)

"""
testlib.c =>
    double func(int n, double args[n]){
        return args[0]*args[0] + args[1]*args[1];}
compile to library testlib.*
"""

# lib = ctypes.CDLL('/home/.../testlib.*')  # use absolute path
#lib.func.restype = ctypes.c_double
#lib.func.argtypes = (ctypes.c_int, ctypes.c_double)
#integrate.quad(lib.func, 0, 1, (1))
#(1.3333333333333333, 1.4802973661668752e-14)
# print((1.0**3 / 3.0 + 1.0) - (0.0**3 / 3.0 + 0.0))  # Analytic result
# 1.3333333333333333


def y(x): return 1 if x <= 0 else 0


print(integrate.quad(y, -1, 1))
print(integrate.quad(y, -1, 100))
print(integrate.quad(y, -1, 10000))
