#!/bin/bash

# Script for starting and getting the submodules (Commit saved in the main repo), 
# doing checkout to the correct branches, and pulling all the submodules from origin.

bold_t="$(tput bold)"        # \033[1m
norm_t="$(tput sgr0)"        # \033[0m

echo -e "${bold_t}[${norm_t}sync-dotfiles${bold_t}] Changing directory...${norm_t}"
cd ..
echo -e "${bold_t}[${norm_t}sync-dotfiles${bold_t}] Updating submodules...${norm_t}\n"
git submodule update --init --recursive
echo -e "\n${bold_t}[${norm_t}sync-dotfiles${bold_t}] Checking out the main branch...${norm_t}\n"
git submodule foreach git checkout main
echo -e "\n${bold_t}[${norm_t}sync-dotfiles${bold_t}] Pulling remote repositories...${norm_t}\n"
git submodule foreach git pull origin main
echo -e "\n${bold_t}[${norm_t}sync-dotfiles${bold_t}] All done!${norm_t}\n"
