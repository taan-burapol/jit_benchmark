set var=%CD%
call %USERPROFILE%/anaconda3/Scripts/activate.bat %USERPROFILE%/anaconda3
call activate nuins-numba
rmdir nuitka_jit.dist /S /Q
mkdir nuitka_jit.dist

call python -m nuitka numpy_py.py --standalone --onefile --enable-plugin=upx --upx-binary=D:\upx-4.0.2-win64 --show-anti-bloat-changes --mingw64

call python -m nuitka nuitka_aot.py --standalone --onefile --enable-plugin=upx --upx-binary=D:\upx-4.0.2-win64 --show-anti-bloat-changes --mingw64

call python -m nuitka nuitka_jit_py.py --standalone --include-module=numba --include-data-file=numba_jit.py=numba_jit.py --mingw64

call python -m nuitka nuitka_jit_pyc.py --standalone --include-module=numba --include-data-file=numba_jit.pyc=numba_jit.pyc --mingw64



XCOPY nuitka_jit_py.dist nuitka_jit.dist /E /Y
XCOPY nuitka_jit_pyc.dist nuitka_jit.dist /E /Y

:pause