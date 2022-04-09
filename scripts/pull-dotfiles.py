# Python script for pulling each submodule

import git

#############################
main_repo_path = ".."       # The location of r4v10l1/dotfiles. Because we are in /scripts, ".."
#############################

# -----------------------------------------------------------------------
# Functions for each repo

def pull_repo_linux():
    repo_path = "%s/linux" % main_repo_path
    repo = git.Repo(repo_path)
    repo_origin = repo.remotes.origin
    print("[Linux] Pulling commits from r4v10l1/arch-files...")
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin")
    repo_origin.pull()
    print("[Linux] Pulled %s commits from origin/main." % commits_to_pull)

def pull_repo_windows():
    repo_path = "%s/windows" % main_repo_path
    repo = git.Repo(repo_path)
    repo_origin = repo.remotes.origin
    print("[Windows] Pulling commits from r4v10l1/cmder-dotfiles...")
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin")
    repo_origin.pull()
    print("[Windows] Pulled %s commits from origin/main." % commits_to_pull)

def pull_repo_browser():
    repo_path = "%s/browser" % main_repo_path
    repo = git.Repo(repo_path)
    repo_origin = repo.remotes.origin
    print("[Browser] Pulling commits from r4v10l1/browser-homepage...")
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin")
    repo_origin.pull()
    print("[Browser] Pulled %s commits from origin/main." % commits_to_pull)

def pull_repo_vim():
    repo_path = "%s/vim" % main_repo_path
    repo = git.Repo(repo_path)
    repo_origin = repo.remotes.origin
    print("[Vim] Pulling commits from r4v10l1/vim-dotfiles...")
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin")
    repo_origin.pull()
    print("[Vim] Pulled %s commits from origin/main." % commits_to_pull)

# -----------------------------------------------------------------------
# Pull each repo

def main():
    pull_repo_linux()
    pull_repo_windows()
    pull_repo_browser()
    pull_repo_vim()

main()
