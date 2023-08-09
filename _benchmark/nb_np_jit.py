import numba as nb
import numpy as np


# force compilation in nopython mode
@nb.jit(nb.int64(nb.types.Array(nb.int64, 1, "A")), forceobj=True)
def sum_of_squares(numbers):
    result = np.sum(numbers * numbers)
    return result


# compiled in object mode
@nb.jit(forceobj=True)
def sum_of_squares_py(n):
    numbers = np.arange(1, n + 1, 1, np.int64)
    result = sum_of_squares(numbers)
    return result
