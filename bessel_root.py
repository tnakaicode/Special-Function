import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn, jv, jve, jvp
from scipy.special import jn_zeros, jnp_zeros
from scipy.special import yn_zeros, ynp_zeros
from scipy.special import jnjnp_zeros, jnyn_zeros

if __name__ == '__main__':
    """Compute zeros of integer-order Bessel function Jn(x).

    Parameters
    ----------
    n : int
        Order of Bessel function
    nt : int
        Number of zeros to return

    References
    ----------
    .. [1] Zhang, Shanjie and Jin, Jianming. "Computation of Special
           Functions", John Wiley and Sons, 1996, chapter 5.
           https://people.sc.fsu.edu/~jburkardt/f_src/special_functions/special_functions.html

    """
    for nth, val in enumerate(jn_zeros(0, 5)):
        txt = "{:d}".format(nth)
        txt += "\t{:.2f}\t{:.2f}\t{:.2f}".format(val, jn(0, val), jn(1, val))
        print(txt)
    for nth, val in enumerate(jn_zeros(1, 5)):
        txt = "{:d}".format(nth)
        txt += "\t{:.2f}\t{:.2f}\t{:.2f}".format(val, jn(0, val), jn(1, val))
        print(txt)
    for nth, val in enumerate(jn_zeros(2, 5)):
        txt = "{:d}".format(nth)
        txt += "\t{:.2f}\t{:.2f}\t{:.2f}".format(val, jn(0, val), jn(1, val))
        txt += "\t{:.2f}".format(jn(2, val))
        print(txt)

    """Compute zeros of integer-order Bessel function derivative Jn'(x).
    """
    print(jnp_zeros(0, 5))
    print(jnp_zeros(1, 5))
    print(jnp_zeros(2, 5))

    """Compute zeros of integer-order Bessel function Yn(x).
    """
    print(yn_zeros(0, 5))
    print(yn_zeros(1, 5))
    print(yn_zeros(2, 5))

    """Compute zeros of integer-order Bessel function derivative Yn'(x).
    """
    print(ynp_zeros(0, 5))
    print(ynp_zeros(1, 5))
    print(ynp_zeros(2, 5))

    """Compute zeros of integer-order Bessel functions Jn and Jn'.

    Parameters
    ----------
    nt : int
        Number (<=1200) of zeros to compute

    Returns
    -------
    zo[l-1] : ndarray
        Value of the lth zero of Jn(x) and Jn'(x). Of length `nt`.
    n[l-1] : ndarray
        Order of the Jn(x) or Jn'(x) associated with lth zero. Of length `nt`.
    m[l-1] : ndarray
        Serial number of the zeros of Jn(x) or Jn'(x) associated
        with lth zero. Of length `nt`.
    t[l-1] : ndarray
        0 if lth zero in zo is zero of Jn(x), 1 if it is a zero of Jn'(x). Of
        length `nt`.

    """
    zo, n, m, t = jnjnp_zeros(5)
    print(*zo)
    print(*n)
    print(*m)
    print(*t)

    """Compute nt zeros of Bessel functions Jn(x), Jn'(x), Yn(x), and Yn'(x).
    """
    print(jnyn_zeros(0, 5))
    print(jnyn_zeros(1, 5))
