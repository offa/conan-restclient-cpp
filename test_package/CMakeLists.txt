cmake_minimum_required(VERSION 3.11)
project(test_package CXX)

find_package(restclient-cpp REQUIRED)

add_executable(test_package example.cpp)
target_link_libraries(test_package PRIVATE restclient-cpp::restclient-cpp)

