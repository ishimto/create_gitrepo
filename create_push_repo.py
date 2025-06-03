import subprocess
from pathlib import Path
from git import Repo
import gitlab
from modules.envs import GITLAB_TOKEN, GITLAB_URL
from modules.create_project import create_gitlab_project


def main():

    user_repo = input("Repo name: ").strip()

    gl = gitlab.Gitlab(GITLAB_URL, private_token=GITLAB_TOKEN)
    gl.auth()

    project = create_gitlab_project(gl, user_repo)

    if not project:
        print("gitlab project failed")
        return

    current_dir = Path.cwd()
    repo_path = current_dir / user_repo
    repo_path.mkdir(exist_ok=True)

    repo = Repo.init(repo_path)
    print(f"initialized local repo: {repo_path}")

    file_path = repo_path / "README.md"
    file_path.write_text("initial commit")

    repo.index.add([str(file_path.name)])
    repo.index.commit("initial commit")
    print("committed initial README.md")

    remote_url = project.http_url_to_repo
    origin = repo.create_remote('origin', remote_url)
    print(f"added remote origin: {remote_url}")

    try:
        origin.push(refspec='main:main')
        print("pushed initial commit to gitlab")
    except Exception as e:
        print(f"push failed: {e}")

    subprocess.run(['code', repo_path])

if __name__ == "__main__":
    main()
