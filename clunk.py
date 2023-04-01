#!/usr/bin/env python

import os

# Prompt the user to enter their C++ code
print("Enter your C++ code:")

# Read lines of input until the user enters a blank line
stuff = ""
while True:
    line = input()
    if line.strip() == "":
        break
    stuff += line + "\n"

# Print the code to verify that it was read correctly
# print("You entered the following code:")
# print(stuff)

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

# print(cpp_code)

with open("main.cpp", "w") as f:
    f.write(cpp_code)

# Compile the C++ source file using g++
os.system("g++ main.cpp -o main")

# Run the resulting executable
os.system("./main")
