# Python script for pulling each submodule

try:
    import git
except Exception:
    print("You need git to use this script! Make sure you run:")
    print("  python3 -m pip install -r requirements.txt")
    exit(1)

try:
    from colorama import Fore, Style
    colorama_found = True
except Exception:
    colorama_found = False

################################
main_repo_path = "../.."       # The location of r4v10l1/dotfiles. Because we are in /scripts/python, "../.."
################################

# -----------------------------------------------------------------------
# Functions for printing with colorama (if found)

def cprint_pulling(repo_color, repo_name, remote_name):
    if colorama_found:
        print("%s%s[%s%s%s%s%s] Pulling commits from %s%s%s...%s" % 
                (Style.RESET_ALL, Fore.WHITE, repo_color, Style.BRIGHT, repo_name, Style.RESET_ALL, Fore.WHITE,
                    repo_color, remote_name, Fore.WHITE, Style.RESET_ALL))
    else:
        print("[%s] Pulling commits from %s..." % (repo_name, remote_name))

def cprint_pulled(repo_color, repo_name, commit_number):
    if colorama_found:
        print("%s%s[%s%s%s%s%s] Pulled %s%s%s commits from origin/main...%s" % 
                (Style.RESET_ALL, Fore.WHITE, repo_color, Style.BRIGHT, repo_name, Style.RESET_ALL, Fore.WHITE,
                    repo_color, commit_number, Fore.WHITE, Style.RESET_ALL))
    else:
        print("[%s] Pulled %s commits from origin/main..." % (repo_name, commit_number))

def cprint_error(error_text):
    if colorama_found:
        print("%s%s[%s%sError%s%s] %s%s" % 
                (Style.RESET_ALL, Fore.WHITE, Fore.RED, Style.BRIGHT, Style.RESET_ALL, Fore.WHITE,
                    error_text, Style.RESET_ALL))
    else:
        print("[Error] %s" % (error_text))

def cprint_error_sugestion():
    if colorama_found:
        print("%s%s[%s%sInfo%s%s] You might want to use %s--recurse-submodules%s when cloning, or run %sscripts/sync-dotfiles.sh%s to easily pull all of them.%s" % 
                (Style.RESET_ALL, Fore.WHITE, Fore.BLUE, Style.BRIGHT, Style.RESET_ALL, Fore.WHITE,
                    Style.BRIGHT, Style.NORMAL, Style.BRIGHT, Style.NORMAL, Style.RESET_ALL))
    else:
        print("[Info] You might want to use --recurse-submodules when cloning, or run scripts/sync-dotfiles.sh to easily pull all of them.")

# -----------------------------------------------------------------------
# Functions for each repo

def pull_repo_linux():
    repo_path = "%s/linux" % main_repo_path
    try:
        repo = git.Repo(repo_path)
    except Exception:
        cprint_error("I can't find a repo in %s..." % (repo_path))
        cprint_error_sugestion()
        exit(1)
    repo_origin = repo.remotes.origin
    cprint_pulling(Fore.BLUE, "Linux", "r4v10l1/arch-dotfiles")
    repo_origin.fetch()
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin/main")
    repo_origin.pull()
    cprint_pulled(Fore.BLUE, "Linux", commits_to_pull)

def pull_repo_windows():
    repo_path = "%s/windows" % main_repo_path
    try:
        repo = git.Repo(repo_path)
    except Exception:
        cprint_error("I can't find a repo in %s..." % (repo_path))
        cprint_error_sugestion()
        exit(1)
    repo_origin = repo.remotes.origin
    cprint_pulling(Fore.CYAN, "Windows", "r4v10l1/cmder-dotfiles")
    repo_origin.fetch()
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin/main")
    repo_origin.pull()
    cprint_pulled(Fore.CYAN, "Windows", commits_to_pull)

def pull_repo_browser():
    repo_path = "%s/browser" % main_repo_path
    try:
        repo = git.Repo(repo_path)
    except Exception:
        cprint_error("I can't find a repo in %s..." % (repo_path))
        cprint_error_sugestion()
        exit(1)
    repo_origin = repo.remotes.origin
    cprint_pulling(Fore.YELLOW, "Browser", "r4v10l1/browser-homepage")
    repo_origin.fetch()
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin/main")
    repo_origin.pull()
    cprint_pulled(Fore.YELLOW, "Browser", commits_to_pull)

def pull_repo_vim():
    repo_path = "%s/vim" % main_repo_path
    try:
        repo = git.Repo(repo_path)
    except Exception:
        cprint_error("I can't find a repo in %s..." % (repo_path))
        cprint_error_sugestion()
        exit(1)
    repo_origin = repo.remotes.origin
    cprint_pulling(Fore.GREEN, "Vim", "r4v10l1/vim-dotfiles")
    repo_origin.fetch()
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin/main")
    repo_origin.pull()
    cprint_pulled(Fore.GREEN, "Vim", commits_to_pull)

# -----------------------------------------------------------------------
# Pull each repo

def main():
    pull_repo_linux()
    pull_repo_windows()
    pull_repo_browser()
    pull_repo_vim()

main()
