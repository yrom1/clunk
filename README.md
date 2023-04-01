# clunk
To use `clunk` enter your C++ code when prompted:
```
(main) Ryans-MacBook-Air:clunk ryan$ clunk
Enter your C++ code:

Hello, world!
(main) Ryans-MacBook-Air:clunk ryan$ clunk
Enter your C++ code:
std::cout << 42 << std::endl;

42
(main) Ryans-MacBook-Air:clunk ryan$ clunk
Enter your C++ code:
std::vector<int> v = {1, 2, 3};

(main) Ryans-MacBook-Air:clunk ryan$ clunk
Enter your C++ code:
std::vector<int> v = {1, 2, 3};
for (int i = 0; i < v.size(); ++i) {
    std::cout << v[i] << " ";
}
std::cout << std::endl;

1 2 3
(main) Ryans-MacBook-Air:clunk ryan$
```
And use `clunkier` if you want to do stuff outside of main:
```
(main) Ryans-MacBook-Air:Tensor.h ryan$ clunkier
Enter the code to be placed above the main function:
#include "Tensor.h"

Enter the code to be placed inside the main function:
Tensor<float> t{3, 4, 2};
t[{1, 1, 1}] = 42.0f;
std::cout << t[{1, 1, 1}] << std::endl;

42
```
Clunk includes all STL headers for you and uses C++20.

# Install
```
(main) Ryans-MacBook-Air:clunk ryan$ . install.sh
clunk installed successfully!
```
```
(main) Ryans-MacBook-Air:clunk ryan$ tail -n 2 ~/.bash_profile
export PATH="$PATH:/Users/ryan/clunk"
alias clunk="clunk.py"
alias clunkier="clunk.py 42"
```
