#!/bin/bash

chmod +x clunk.py

# Add the clunk command to your system path
echo 'export PATH="$PATH:'"$PWD"'"' >> ~/.bash_profile
source ~/.bash_profile

echo "clunk command installed successfully!"
