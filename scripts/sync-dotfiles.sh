#!/bin/bash

# Script for doing checkout to the correct branches, and pulling all the submodules

echo "Changing directory..."
cd ..
echo "Updating submodules..."
git submodule update --init --recursive
echo "Checking out the main branch..."
git submodule foreach git checkout main
echo "Pulling remote repositories..."
git submodule foreach git pull origin main
echo "All done!"
