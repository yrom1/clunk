# clunk
To use clunk, simply run the `clunk.py` script and enter your C++ code when prompted:

```
Ryans-MacBook-Air:~ ryan$ clunk
Enter your C++ code:
#include <iostream>
std::cout << 42 << std::endl;

42
Ryans-MacBook-Air:~ ryan$
```

# Install
```
(main) Ryans-MacBook-Air:clunk ryan$ . install.sh
clunk installed successfully!
(main) Ryans-MacBook-Air:clunk ryan$ tail -n 2 ~/.bash_profile
export PATH="$PATH:/Users/ryan/clunk"
alias clunk="clunk.py"
```
