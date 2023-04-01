#!/usr/bin/env python

import os

# Create a C++ source file with a main function
cpp_code = """
#include <iostream>

int main() {
    std::cout << "Hello, world!" << std::endl;
    return 0;
}
"""

with open("main.cpp", "w") as f:
    f.write(cpp_code)

# Compile the C++ source file using g++
os.system("g++ main.cpp -o main")

# Run the resulting executable
os.system("./main")
