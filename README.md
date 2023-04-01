# clunk
To use clunk, simply run the `clunk.py` script and enter your C++ code when prompted:

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

(main) Ryans-MacBook-Air:clunk ryan$
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
```
