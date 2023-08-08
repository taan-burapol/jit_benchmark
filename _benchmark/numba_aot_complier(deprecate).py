import numba as nb
from numba.pycc import CC

# Create a compiler object
cc = CC('numba_aot_lib')


# Add the function to the compiler
@cc.export('square', 'i8(i8)')
def sum_of_squares_py(n):
    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result


cc.compile()
