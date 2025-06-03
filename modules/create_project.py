import gitlab

def create_gitlab_project(gl, project_name):
    try:
        project_data = {
            'name': project_name,
            'visibility': 'private',
        }

        project = gl.projects.create(project_data)
        return project

    except Exception as e:
        print(f"gitlab project failed: {e}")
