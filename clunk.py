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
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <chrono>
#include <cmath>
#include <complex>
#include <condition_variable>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <mutex>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <random>
#include <ratio>
#include <regex>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeinfo>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <valarray>

int main() {{
    {stuff}
    return 0;
}}\
"""

# print(cpp_code)

with open("main.cpp", "w") as f:
    f.write(cpp_code)

# Compile the C++ source file using g++
os.system("g++ -std=c++20 main.cpp -o main")

# Run the resulting executable
os.system("./main")
