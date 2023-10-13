#!/bin/bash

# Commits each submodule. stdout is disabled for ignoring errors,
# keep that in mind.

cd ..

commit() {
    git add $1 1>/dev/null
    git commit -m "Update $1 repo" 1>/dev/null
}

commit "browser"
commit "linux"
commit "vim"
commit "emacs"
commit "windows"
