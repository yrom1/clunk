#!/usr/bin/env python

import os

stuff = input("Enter your C++ code:\n")

if stuff == "":
    stuff = '#include <iostream>\n    std::cout << "Hello, world!" << std::endl;'

# Create a C++ source file with a main function
cpp_code = f"""
#include <iostream>

int main() {{
    {stuff}
    return 0;
}}\
"""

print(cpp_code)

with open("main.cpp", "w") as f:
    f.write(cpp_code)

# Compile the C++ source file using g++
os.system("g++ main.cpp -o main")

# Run the resulting executable
os.system("./main")
