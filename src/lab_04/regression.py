# src/lab_04/regression.py
import numpy as np

def multi_regress(y, Z):
    """
    Perform multiple linear regression.

    Parameters
    ----------
    y : array_like, shape = (n,) or (n,1)
        The vector of dependent variable data
    Z : array_like, shape = (n,m)
        The matrix of independent variable data

    Returns
    -------
    numpy.ndarray, shape = (m,)
        The vector of model coefficients
    numpy.ndarray, shape = (n,)
        The vector of residuals
    float
        The coefficient of determination, r^2
    """
    y = np.asarray(y).flatten()
    Z = np.asarray(Z)

    # Add a column of ones to Z for the intercept term
    Z_aug = np.hstack([np.ones((Z.shape[0], 1)), Z])

    # Least squares solution
    a = np.linalg.lstsq(Z_aug, y, rcond=None)[0]

    # Model output
    f = Z_aug @ a
    e = y - f

    # Coefficient of determination
    ss_res = np.sum(e**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - ss_res / ss_tot

    return a, e, r_squared