#!/bin/bash

if [ ! -e "clunk.py" ]; then
  echo "Error: clunk.py file not found in $(pwd)" >&2
  return 1
fi

chmod +x clunk.py

echo 'export PATH="$PATH:'"$PWD"'"' >> ~/.bash_profile
echo 'alias clunk="clunk.py"' >> ~/.bash_profile
source ~/.bash_profile

echo "clunk installed successfully!"
