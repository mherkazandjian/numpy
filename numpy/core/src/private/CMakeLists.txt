#include_directories(${PROJECT_SOURCE_DIR}/"include")

include_directories(${PYTHON_INCLUDE_DIRS})

add_library(private.so
            lowlevel_strided_loops.h
            mem_overlap.c
            mem_overlap.h
            npy_binsearch.h
            npy_binsearch.h.src
            npy_cblas.h
            npy_config.h
            npy_extint128.h
            npy_fpmath.h
            npy_import.h
            npy_partition.h
            npy_partition.h.src
            npy_pycompat.h
            npy_sort.h
            templ_common.h
            templ_common.h.src
            ufunc_override.h)
