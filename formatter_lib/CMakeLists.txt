cmake_minimum_required(VERSION 3.4)

set(CMAKE_CXX_STANDART 11)

project(formatter)

add_library(formatter STATIC ${CMAKE_CURRENT_SOURCE_DIR}/formatter.cpp)
