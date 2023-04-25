#!/bin/bash

# Commits each submodule. stdout is disabled for ignoring errors,
# keep that in mind.

cd ..

git add browser
git commit -m "Update browser repo" 1>/dev/null
git add linux 1>/dev/null
git commit -m "Update linux repo" 1>/dev/null
git add vim 1>/dev/null
git commit -m "Update vim repo" 1>/dev/null
git add emacs 1>/dev/null
git commit -m "Update emacs repo" 1>/dev/null
git add windows 1>/dev/null
git commit -m "Update windows repo" 1>/dev/null
