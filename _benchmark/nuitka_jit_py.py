import os
import csv
import sys
import timeit

FILENAME = "numba_jit"


def execute_bytecode(bytecode, globals_dict, locals_dict):
    try:
        exec(bytecode, globals_dict, locals_dict)
    except Exception as e:
        print(f"Error executing the bytecode: {e}")


def write_csv_with_loop(iterations, filename):
    # Python script for execute
    script_path = os.path.join(os.path.dirname(sys.argv[0]), FILENAME + ".py")

    with open(script_path, 'r') as script_file:
        script_code = script_file.read()
    if script_code:
        # Define the globals and locals dictionaries with arguments
        globals_dict = {}
        locals_dict = {}  # The argument to example_function

        # Execute the bytecode with arguments
        execute_bytecode(script_code, globals_dict, locals_dict)

        # Call the example_function from the executed code
        if 'sum_of_squares_py' in locals_dict:
            benchmark = locals_dict['sum_of_squares_py']
            with open(filename, mode='w', newline='') as script_file:
                writer = csv.writer(script_file)
                writer.writerow(['Iterations Number', 'Elapsed Time'])

                for i in range(1, iterations + 1):
                    size = 2 ** i
                    elapsed = timeit.timeit(lambda: benchmark(size), number=10)
                    writer.writerow([size, elapsed])
                    print(f'Writing Iterations Number {i} and Elapsed Time {elapsed} to {filename}')


if __name__ == "__main__":
    num_iterations = int(input("num_iterations :"))  # Change this number to the desired number of iterations
    csv_filename = FILENAME + '_py' + '.csv'  # Change this to the desired filename

    write_csv_with_loop(num_iterations, csv_filename)
