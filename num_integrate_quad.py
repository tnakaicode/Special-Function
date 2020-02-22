import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from scipy.integrate import quad_vec, quadrature
from scipy.interpolate import splprep, splrep, splev

"""
   quad          -- General purpose integration
   quad_vec      -- General purpose integration of vector-valued functions
   dblquad       -- General purpose double integration
   tplquad       -- General purpose triple integration
   nquad         -- General purpose n-dimensional integration
   fixed_quad    -- Integrate func(x) using Gaussian quadrature of order n
   quadrature    -- Integrate with given tolerance using Gaussian quadrature
   romberg       -- Integrate func using Romberg integration
   quad_explain  -- Print information for use of quad
   newton_cotes  -- Weights and error coefficient for Newton-Cotes integration
   trapz         -- Use trapezoidal rule to compute integral.
   cumtrapz      -- Use trapezoidal rule to cumulatively compute integral.
   simps         -- Use Simpson's rule to compute integral from samples.
   romb          -- Use Romberg Integration to compute integral from
                 -- (2**k + 1) evenly-spaced samples.
"""


def f(x): return x**8


if __name__ == '__main__':
    print(*quadrature(f, 0.0, 1.0))
    print(1/9.0)  # analytical result
    print(*quadrature(np.cos, 0.0, np.pi/2))
    print(np.sin(np.pi/2)-np.sin(0))  # analytical result

    x = np.linspace(0, 10, 10)
    y = np.sin(x)
    spl = splrep(x, y)
    x2 = np.linspace(0, 10, 200)
    y2 = splev(x2, spl)

    plt.figure()
    plt.plot(x, y, 'o')
    plt.plot(x2, y2)
    plt.grid()
    plt.show()
