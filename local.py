import sys
import os


def local_project(project):
    try:
        folder = os.environ['ProjectPath']
    except:
        print("Create project folder in environment variables.")
        sys.exit()


    if os.path.isdir(folder):

        project_path = os.path.join(folder, project)

        if os.path.exists(project_path):
            while os.path.exists(project_path):
                project = input("Project name already exists. Please enter a different project name:")
                project_path = os.path.join(folder, project)

        os.mkdir(project_path)

        commands = [f'echo "# {project}" >> README.md',
                    'git init',
                    'git add *',
                    'git commit -m "committing readme file"']

        os.chdir(project_path)
        for c in commands:
            os.system(c)

        return project_path

    else:
        print("Please set a valid project folder name in environment variables.")
