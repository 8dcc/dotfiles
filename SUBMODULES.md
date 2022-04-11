# My experience with submodules

### Configuring submodules with remote branch
Thanks to stackoverflow ([Link](https://stackoverflow.com/questions/18770545/why-is-my-git-submodule-head-detached-from-master)).  
When creating submodules:
```bash
git submodule add -b <branch> <repository> [<submodule-path>]
git config -f .gitmodules submodule.<submodule-path>.update rebase
git submodule update --remote
```
When updating submodules (my case):
```bash
cd <submodule-path>
git checkout <branch>
cd <parent-repo-path>
<submodule-path> is here path releative to parent repo root
without starting path separator
git config -f .gitmodules submodule.<submodule-path>.branch <branch>
git config -f .gitmodules submodule.<submodule-path>.update <rebase|merge>
```

### Pulling repositories
I made a script for pulling all repositories, but maybe the user did not download with `--recurse-submodules` or the `HEAD` is detached.  
There is also a git command for doing this:
```bash
git submodule update --init --recursive         # Git command
```
Check the [main readme](https://github.com/r4v10l1/dotfiles#pulling-the-repositories) for more info.
