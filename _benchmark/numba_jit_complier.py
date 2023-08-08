import marshal


def read_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


def compile_python_to_bytecode(source_code):
    try:
        bytecode = compile(source_code, filename="<string>", mode="exec")
        return bytecode
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
        return None


def save_bytecode_to_pyc(bytecode, pyc_file_path):
    try:
        with open(pyc_file_path, "wb") as pyc_file:
            marshal.dump(bytecode, pyc_file)
        print(f"Bytecode saved to {pyc_file_path}")
    except Exception as e:
        print(f"Error saving the bytecode: {e}")


# Path to the file you want to read and compile
file_path = "numba_jit.py"

# Read the content of the file
source_code = read_file_content(file_path)

# Check if the file was read successfully
if source_code:
    # Compile the source code to bytecode
    bytecode = compile_python_to_bytecode(source_code)

    # Check if the compilation was successful
    if bytecode:
        # Save bytecode to a .pyc file
        pyc_file_path = "numba_jit.pyc"
        save_bytecode_to_pyc(bytecode, pyc_file_path)
    else:
        print("Compilation failed.")
else:
    print("Failed to read the source code.")
