#!/usr/bin/env python

import os
import sys

# Check if a flag is passed to the script
if len(sys.argv) > 1:
    # Read lines of input until the user enters a blank line for code to be placed above the main function
    print("Enter the code to be placed above the main function:")
    code_above_main = ""
    while True:
        line = input()
        if line.strip() == "":
            break
        code_above_main += line + "\n"

    # Read lines of input until the user enters a blank line for code to be placed inside the main function
    print("Enter the code to be placed inside the main function:")
    code_inside_main = ""
    while True:
        line = input()
        if line.strip() == "":
            break
        code_inside_main += line + "\n"
else:
    code_above_main = ""
    # Prompt the user to enter their C++ code
    print("Enter your C++ code:")
    code_inside_main = ""
    while True:
        line = input()
        if line.strip() == "":
            break
        code_inside_main += line + "\n"

if code_inside_main == "":
    code_inside_main = 'std::cout << "Hello, world!" << std::endl;'


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

{code_above_main}

int main() {{
    {code_inside_main}
    return 0;
}}\
"""

with open("main.cpp", "w") as f:
    f.write(cpp_code)

# Compile the C++ source file using g++
os.system("g++ -std=c++20 main.cpp -o main")

# Run the resulting executable
os.system("./main")
