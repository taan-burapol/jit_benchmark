import numba as nb
import numpy as np


@nb.jit(nopython=True)
def sum_of_squares_py(n):
    numbers = np.arange(1, n + 1)
    result = np.sum(numbers * numbers)
    return result
