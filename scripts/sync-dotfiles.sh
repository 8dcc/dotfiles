#!/usr/bin/env bash
#
# Script for starting and getting the submodules (Commit saved in the main
# repo), doing checkout to the correct branches, and pulling all the submodules
# from origin.

BOLD_T="$(tput bold)"        # \033[1m
NORM_T="$(tput sgr0)"        # \033[0m
log() {
    echo -e "${BOLD_T}[${NORM_T}sync-dotfiles${BOLD_T}] ${1}${NORM_T}"
}

log 'Changing directory...'
cd "$(dirname -- "$(readlink -f -- "${BASH_SOURCE[0]}")")/.." || exit 1
log 'Updating submodules...'
git submodule update --init --recursive
log 'Checking out the main branch...'
git submodule foreach git checkout main
log 'Pulling remote repositories...'
git submodule foreach git pull origin main
log 'All done!'
