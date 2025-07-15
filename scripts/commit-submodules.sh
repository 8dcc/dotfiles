#!/usr/bin/env bash
#
# Commits each submodule. stdout is disabled for ignoring errors,
# keep that in mind.

commit() {
    git add "$1" 1> /dev/null
    git commit -m "Update $1 repo" 1> /dev/null
}

cd "$(dirname -- "$(readlink -f -- "${BASH_SOURCE[0]}")")/.." || exit 1
commit 'browser'
commit 'linux'
commit 'vim'
commit 'emacs'
commit 'windows'
echo 'All done.'
