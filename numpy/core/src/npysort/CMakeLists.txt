#include_directories(${PROJECT_SOURCE_DIR}/"include")

include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(../private)

add_library(npysort.so
            binsearch.c
            binsearch.c.src
            CMakeLists.txt
            heapsort.c
            heapsort.c.src
            mergesort.c
            mergesort.c.src
            npysort_common.h
            quicksort.c
            quicksort.c.src
            selection.c
            selection.c.src)