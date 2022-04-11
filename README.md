# Personal dotfiles
**My personal dotfiles**

### Cloning
Because this repository has [submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules), you need to specify a parameter to the git clone command ([?](http://git-scm.com/book/en/v2/Git-Tools-Submodules#_cloning_submodules)):
```bash
git clone --recurse-submodules https://github.com/r4v10l1/dotfiles
```
Check [SUBMODULES.md](https://github.com/r4v10l1/dotfiles/blob/main/SUBMODULES.md) for more info.

### Pulling the repositories
Once you have them downloaded, there might be changes to the submodules! And if you do a `git pull` on the dotfiles repository, you will not pull the submodules.  
To do this, use the `git submodules` command 
```bash
git submodule update --init --recursive         # Git command
```
Or use my python script (See [scripts](#scripts)):
```bash
cd scripts
python3 -m pip install -r requirements.txt
python3 pull-dotfiles.py
```
**Or you can do all that at once, even if you did not use `--recurse-submodules` with my bash script:**
```bash
cd scripts
chmod +x sync-dotfiles.sh
./sync-dotfiles.sh
```

### Scripts
Before using the scripts make sure you have all the requirements installed with:
```bash
cd scripts
python3 -m pip install -r requirements.txt
```

#### `pull-dotfiles.py`
This script will pull each submodule on the repo.

#### `sync-dotfiles.sh`
This script updates the submodules, does checkout to the main branch, and pulls the repositories.
