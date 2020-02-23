# Scipy Special Function

Scipy-Polynomial

- Legendre polynomial.
- Chebyshev polynomial of the first kind.
- Chebyshev polynomial of the second kind.
- Chebyshev polynomial of the first kind on [-2,2].
- Chebyshev polynomial of the second kind on [-2,2].
- Jacobi polynomial.
- Laguerre polynomial.
- Generalized (associated) Laguerre polynomial.
- Physicist’s Hermite polynomial.
- Normalized (probabilist’s) Hermite polynomial.
- Gegenbauer (ultraspherical) polynomial.
- Shifted Legendre polynomial.
- Shifted Chebyshev polynomial of the first kind.
- Shifted Chebyshev polynomial of the second kind.
- Shifted Jacobi polynomial.

Scipy

- Clustering package (scipy.cluster)
- Constants (scipy.constants)
- Discrete Fourier transforms (scipy.fft)
- Legacy discrete Fourier transforms (scipy.fftpack)
- Integration and ODEs (scipy.integrate)
- Interpolation (scipy.interpolate)
- Input and output (scipy.io)
- Linear algebra (scipy.linalg)
- Miscellaneous routines (scipy.misc)
- Multi-dimensional image processing (scipy.ndimage)
- Orthogonal distance regression (scipy.odr)
- Optimization and Root Finding (scipy.optimize)
- Signal processing (scipy.signal)
- Sparse matrices (scipy.sparse)
- Sparse linear algebra (scipy.sparse.linalg)
- Compressed Sparse Graph Routines (scipy.sparse.csgraph)
- Spatial algorithms and data structures (scipy.spatial)
- Special functions (scipy.special)
- Statistical functions (scipy.stats)
- Statistical functions for masked arrays (scipy.stats.mstats)
- Low-level callback functions

## $\Gamma$ Function

Euler
$$ \Gamma (z) = \int_0^{\infty} e^{-t} t^{z-1} dt (Re(z) > 0) $$
$$ \Gamma' (z) = \int_0^{\infty} e^{-t} t^{z-1} \ln(t) dt $$

$$ t^{z-1} = e^{(z-1)\ln(t)} $$
$$ \Gamma(z) = \frac{1}{z}\Gamma(z+1)$$
$$ \Gamma(n+1) = n! $$
$$ \Gamma(z) = \frac{\Gamma(z+n+1)}{z(z+1)...(z+n)} $$

Hankel
$$ \Gamma (z) = \frac{1}{2i\sin(\pi z)} \int_L e^{-t} (e^{-i\pi})^{z-1} dt $$

Path L starts from $+\infty$ on the real axis at a declination of 0, and returns to $+\infty$ again at a declination of $2\pi$.

## $\Beta$ Function

$$ \Beta (p,q) = \int_0^{1} x^{p-1} (1-x)^{q-1} dx $$
$$ p \Beta (p,q) = q \Beta(p+1,q) $$

$x\sin^2(\theta)=t^2=t/(1+t)$
$$ \begin{aligned}
   \Beta (p,q) &= 2 \int_0^{\pi/2} (\sin\theta)^{2p-1} (\cos\theta)^{2q-1} d\theta \\
   &= 2 \int_0^{1} t^{2p-1} (1-t^2)^{q-1} dt \\
   &= \int_0^{\infty} \frac{t^{p-1}}{(1+t)^{p+q}} dt \\
   &= \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}
\end{aligned}$$

$$\begin{aligned}
    \Beta (z, 1-z) &= \frac{\Gamma(z)\Gamma(1-z)}{\Gamma(1)} \\
    &= \int_0^{\infty} \frac{x^{z-1}}{1+x} dx \\
    &= \frac{\pi}{\sin(\pi z)}
\end{aligned}$$

Pochhammer Integral representation
$$ \Beta(p,q) = \frac{-e^{-i\pi(p+q)}}{4\sin(\pi p)\sin(\pi q)} \int_C t^{p-1} (1-t)^{q-1} dt $$

## $\zeta$ Function

$$ \begin{aligned}
    \zeta(z)
    &= \Sigma_{k=1}^{\infty} \frac{1}{k^z} (Re(z)>1) \\
    &= \frac{1}{\Gamma(z)} \int_0^{\infty} \frac{t^{z-1}}{e^t-1} dt \\
    &= \frac{1}{2\pi} \Gamma(1-z) \int_{L'} \frac{(-t)^{z-1}}{e^t-1} dt
\end{aligned} $$

## Bessel Function

## Hermite Polynomial

Generating function of Hermite Function
$$ \begin{aligned}
    g(t, x) &\equiv
    e^{2 t x - t^2} \\
    &= \Sigma_{n=0}^{\infty} H_n(x) \frac{t^n}{n!}
\end{aligned} $$

$$ \begin{aligned}
    H_n(x) &= \Sigma_{r=0}^{\lfloor n/2 \rfloor} (-1)^r \frac{n!}{r!(n-2r)!} (2x)^{n-2r} \\
    H_0(x) &= 1 \\
    H_1(x) &= 2x \\
    H_2(x) &= 4x^2 - 2 \\
    H_3(x) &= 8x^3 - 12x \\
    H_4(x) &= 16x^4 - 48x^2 + 12
\end{aligned} $$

Recurrence formula of Hermite
$$ \begin{aligned}
    H_{n+1}(x) &= 2x H_n(x) -2n H_{n-1}(x) \\
    H_n'(x)    &= 2n H_{n-1}(x) \\
    H_n'(x)    &= 2x H_n(x) - 2n H_{n+1}(x)
\end{aligned} $$

Orthogonality
$$ \int_{-\infty}^{\infty} H_m(x) H_n(x) e^{-x^2} dx = \sqrt{\pi} 2^n n! \delta_{mn} $$

Summary of proof

$$ \begin{aligned}
    e^{2tx-t^2} e^{2sx-s^2} &= \Sigma_{m=0}^{\infty} \Sigma_{n=0}^{\infty} H_m(x) H_n(x) \frac{t^m s^n}{m! n!} \\
    e^{2tx-t^2} e^{2sx-s^2} e^{-x^2} &= \Sigma_{m=0}^{\infty} \Sigma_{n=0}^{\infty} H_m(x) H_n(x) \frac{t^m s^n}{m! n!} e^{-x^2} \\
    e^{2(t+s)x-x^2-(t^2+s^2)} &= \\
    \int e^{2(t+s)x-x^2-(t^2+s^2)} dx &= \Sigma_{m=0}^{\infty} \Sigma_{n=0}^{\infty} \frac{t^m s^n}{m! n!} \int H_m(x) H_n(x) e^{-x^2} dx \\
    \int e^{-(x-(t+s))^2 +2ts} dx &= e^{2ts} \sqrt{\pi}
    = \sqrt{\pi} \Sigma_{n=0}^{\infty} \frac{2^n}{n!} t^n s^n \\
    \Sigma_{m=0}^{\infty} \Sigma_{n=0}^{\infty} \frac{t^m s^n}{m! n!} \int H_m(x) H_n(x) e^{-x^2} dx &= \sqrt{\pi} \Sigma_{n=0}^{\infty} \frac{2^n}{n!} t^n s^n & (\forall s, t) \\
\end{aligned} $$

Eigenfunction of one-dimensional harmonic oscillator
$$ u_n(x) = \frac{1}{\sqrt{\sqrt{\pi} 2^n n!}} H_n(x) \exp(-\frac{x^2}{2}) $$

Integral Representation
$$ H_n(x) = \frac{1}{\sqrt{\pi}} \int e^{-u^2} (2x + 2i u)^n du $$

Completeness
$$ \Sigma u_n(x) u_n(y) = \delta(x-y) $$
