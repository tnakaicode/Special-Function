import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from scipy.integrate import quad_vec, quadrature

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

if __name__ == '__main__':
    px = np.linspace(0.001, 1, 200)*np.pi
    py = np.sin(px)
    print(simps(py, px))

    def f(x): return x**8
    print(quadrature(f, 0.0, 1.0))
    print(1/9.0)  # analytical result
    print(quadrature(np.cos, 0.0, np.pi/2))
    print(np.sin(np.pi/2)-np.sin(0))  # analytical result

    plt.figure()
    plt.plot(px, py)
    plt.grid()
    plt.show()
