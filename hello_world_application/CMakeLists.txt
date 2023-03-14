cmake_minimum_required(VERSION 3.4)

set(CMAKE_CXX_STANDARD 11)

project(hello_world)

add_executable(hello ${CMAKE_CURRENT_SOURCE_DIR}/hello_world.cpp)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../formatter_ex_lib)
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../formatter_ex_lib formatter_ex)

target_link_libraries(hello formatter_ex)
