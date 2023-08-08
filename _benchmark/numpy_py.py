import csv
import timeit
import numpy as np

FILENAME = "numpy_py"


def sum_of_squares_py(n):
    numbers = np.arange(1, n + 1)
    result = np.sum(numbers * numbers)
    return result


def write_csv_with_loop(iterations, filename):
    with open(filename, mode='w', newline='') as script_file:
        writer = csv.writer(script_file)
        writer.writerow(['Iterations Number', 'Elapsed Time'])

        for i in range(1, iterations + 1):
            size = 2 ** i
            elapsed = timeit.timeit(lambda: sum_of_squares_py(size), number=10)
            writer.writerow([size, elapsed])
            print(f'Writing Iterations Number {i} and Elapsed Time {elapsed} to {filename}')


if __name__ == "__main__":
    num_iterations = int(input("num_iterations :"))  # Change this number to the desired number of iterations
    csv_filename = FILENAME + '.csv'  # Change this to the desired filename

    write_csv_with_loop(num_iterations, csv_filename)
