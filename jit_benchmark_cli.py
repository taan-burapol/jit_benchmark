import numba as nb
import timeit


# Original Python function
def sum_of_squares_py(n):
    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result


# Numba JIT-compiled function
@nb.jit(nopython=True)
def sum_of_squares_numba(n):
    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result


# Compile the Python function using Numba's JIT decorator
jit_sum_of_squares = nb.jit(sum_of_squares_py)

# Accessing the original Python function from JIT-compiled function
original_sum_of_squares = jit_sum_of_squares.py_func


# Benchmarking the original Python function
def benchmark_original(n):
    return sum_of_squares_py(n)


# Benchmarking the JIT-compiled function
def benchmark_jit(n):
    return sum_of_squares_numba(n)


# Measure the average execution time using timeit
size_sum = int(5000000)
num_runs = int(5)
original_time = timeit.timeit(lambda: benchmark_original(size_sum), number=num_runs)
jit_time = timeit.timeit(lambda: benchmark_jit(size_sum), number=num_runs)

print("Time taken by the original Python function:", original_time)
print("Time taken by the JIT-compiled function:", jit_time)
