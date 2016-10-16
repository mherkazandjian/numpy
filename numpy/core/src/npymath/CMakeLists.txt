#include_directories(${PROJECT_SOURCE_DIR}/"include")

include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(../private)

add_library(npymath.so
            halffloat.c
            ieee754.c
            ieee754.c.src
            npy_math.c
            npy_math_common.h
            npy_math_complex.c
            npy_math_complex.c.src
            npy_math.c.src
            npy_math_private.h
            _signbit.c)
