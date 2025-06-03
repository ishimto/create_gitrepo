# Create and Push GitLab Repo

This project provides a Python script that automates the creation of a new GitLab repository and pushes an initial commit, all based on user input.

## What the Script Does

- Prompts you for a repository name.
- Creates a new private project on your GitLab instance using your personal access token.
- Creates a local directory with the same name as your new repo.
- Initializes a local git repository in that directory.
- Adds a `README.md` file with "initial commit" as its content.
- Makes the initial commit and pushes it to the new GitLab repository (on the `main` branch).
- Opens the new project folder in VS Code.

**You do NOT need to manually create or clone the repository. The script handles everything.**

## Setup


### 1. Clone the repository

```bash
git clone https://github.com/ishimto/create_gitrepo.git
cd create_gitrepo
```

### 2. Create and Activate a Virtual Environment

```sh
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Required Environment Variables

Set your GitLab instance URL and personal access token:

```sh
export GITLAB_URL="https://gitlab.com"
export GITLAB_TOKEN="your_personal_access_token"
```

You can add these lines to your shell profile (e.g., `.bashrc` or `.zshrc`) for convenience.

## Usage

Run the script:

```sh
python create_push_repo.py
```

- The script will prompt you for the repository name.
- It will create the project on GitLab, set up the local repo, and push the initial commit.

## Notes

- The script assumes the default branch is `main`.
- Make sure the `code` command (VS Code) is available in your PATH if you want the script to open the new directory automatically.

---
