import tkinter as tk
import tkinter.ttk as ttk
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


# Benchmarking the original Python function
def benchmark_py(n, progress_var):
    for i in range(1, n + 1):
        sum_of_squares_py(n)
        progress_var.set((i / n) * 100)
        root.update_idletasks()
    return n


# Benchmarking the Numba JIT-compiled function
def benchmark_numba(n, progress_var):
    for i in range(1, n + 1):
        sum_of_squares_numba(n)
        progress_var.set((i / n) * 100)
        root.update_idletasks()
    return


def run_benchmarks():
    n = 5000
    run_num = 1

    py_progress_var = tk.DoubleVar()
    py_progress_bar["variable"] = py_progress_var
    py_progress_var.set(0)

    numba_progress_var = tk.DoubleVar()
    numba_progress_bar["variable"] = numba_progress_var
    numba_progress_var.set(0)

    # init JIT for numba
    timeit.timeit(lambda: sum_of_squares_numba(1), number=10)

    py_time = timeit.timeit(lambda: benchmark_py(n, py_progress_var), number=run_num)
    numba_time = timeit.timeit(lambda: benchmark_numba(n, numba_progress_var), number=run_num)

    result_label.config(text=f"Original Python: {py_time:.6f} sec\nNumba JIT: {numba_time:.6f} sec")
    py_progress_bar.stop()
    numba_progress_bar.stop()


root = tk.Tk()
root.title("Numba Benchmark")
root.geometry("400x150")

start_button = tk.Button(root, text="Start Benchmark", command=run_benchmarks)
start_button.pack(pady=10)

py_progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
py_progress_bar.pack()

numba_progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
numba_progress_bar.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
