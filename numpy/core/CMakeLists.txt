cmake_minimum_required (VERSION 3.0)
project (NUMPY)

find_package(PythonLibs 2.7 REQUIRED)
set(PYTHON_EXECUTABLE "/progs/prerequisites/bin/python2.7")
set(PYTHON_LIBRARIES "/progs/prerequisites/lib/libpython2.7.so")
set(PYTHON_INCLUDE_DIRS "/progs/prerequisites/include/python2.7")

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Werror")
set(CMAKE_VERBOSE_MAKEFILE 1)

add_subdirectory(src/multiarray)
#add_subdirectory("src/npymath")
#add_subdirectory("src/npysort")
#add_subdirectory("src/private")
#add_subdirectory("src/umath")

#add_subdirectory (MathFunctions)
#  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)

# add the executable
#target_link_libraries (Tutorial MathFunctions)

