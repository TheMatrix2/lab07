cmake_minimum_required(VERSION 3.4)

set(CMAKE_CXX_STANDART 11)

project(solver_lib)

add_library(solver_lib STATIC ${CMAKE_CURRENT_SOURCE_DIR}/solver.cpp)
