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


class spl_2d (object):

    def __init__(self):
        super().__init__()
        x0 = np.linspace(0, 10, 50)
        y0 = np.linspace(0, 10, 25)
        self.mesh = np.meshgrid(x0, y0)
        self.data = np.sin(self.mesh[0]) + np.cos(self.mesh[1])

        x1 = np.linspace(1, 9, 100)
        y1 = np.linspace(1, 9, 200)
        self.g_mesh = np.meshgrid(x1, y1)

    def fit_2d(self, indx=5):
        X = self.mesh[0].flatten()
        Y = self.mesh[1].flatten()
        A = [np.ones_like(X)]
        for i in range(1, indx):
            for j in range(i + 1):
                ix, iy = j, i - j
                A.append(X**(ix) * Y**(iy))

        A = np.array(A).T
        B = self.data.flatten()
        coeff, r, rank, s = np.linalg.lstsq(A, B)
        print(coeff)
        print(r)
        print(s)

        X = self.g_mesh[0].flatten()
        Y = self.g_mesh[1].flatten()
        A = [np.ones_like(X)]
        for i in range(1, indx):
            for j in range(i + 1):
                ix, iy = j, i - j
                A.append(X**(ix) * Y**(iy))
        A = np.array(A).T
        data = np.zeros_like(X)
        for i, c in enumerate(coeff):
            data += A[:, i] * c
        return data.reshape(self.g_mesh[0].shape)

    def spline(self, x=0):
        return splev(x, self.spl)

    def spline_quad(self):
        return quadrature(self.spline, 0, 15)

    def plot(self):
        x0 = self.mesh[0].flatten()
        y0 = self.mesh[1].flatten()
        z0 = self.data.flatten()
        plt.figure()
        #plt.contourf(*self.mesh, self.data)
        plt.tricontourf(x0, y0, z0)
        plt.grid()

        x1 = self.g_mesh[0].flatten()
        y1 = self.g_mesh[1].flatten()
        z1 = self.fit_2d().flatten()
        plt.figure()
        #plt.contourf(*self.mesh, self.data)
        plt.tricontourf(x1, y1, z1)
        plt.grid()
        plt.show()


if __name__ == '__main__':
    print(*quadrature(f, 0.0, 1.0))
    print(1/9.0)
    print(*quadrature(np.cos, 0.0, np.pi/2))
    print(np.sin(np.pi/2)-np.sin(0))

    obj = spl_2d()
    obj.plot()
