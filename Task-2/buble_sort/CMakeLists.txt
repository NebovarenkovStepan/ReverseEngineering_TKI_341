cmake_minimum_required(VERSION 3.12)

# Имя проекта
project(ReverseEngineeringTask LANGUAGES CXX)

# Указываем стандарт C++ (17 или 20 подойдет)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Создаем исполняемый файл
# "buble_sort_cmake_64" - это будет имя exe файла (my_program.exe)
# "buble_sort.cpp" - ваш исходник
add_executable(my_program buble_sort.cpp)

# (Опционально) Настройка для уменьшения размера GCC (как strip) в Release
if(MINGW AND CMAKE_BUILD_TYPE STREQUAL "Release")
    add_link_options("-s")
endif()