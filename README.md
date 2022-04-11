# Personal dotfiles
**My personal dotfiles**

### Cloning
Because this repository has [submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules), you need to specify a parameter to the git clone command ([?](http://git-scm.com/book/en/v2/Git-Tools-Submodules#_cloning_submodules)):
```bash
git clone --recuse-submodules https://github.com/r4v10l1/dotfiles
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

### Scripts
Before using the scripts make sure you have all the requirements installed with:
```bash
cd scripts
python3 -m pip install -r requirements.txt
```

#### `pull-dotfiles.py`
This script will pull each submodule on the repo.
