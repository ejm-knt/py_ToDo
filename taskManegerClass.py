class ProjectManager:
    def __init__(self):
        self.projects = {}  # 各プロジェクトを格納するディクショナリ

    # プロジェクトを追加する
    def add_project(self, name):
        if not (name in self.projects) :
            self.projects[name] = []
        else:
            print(f"プロジェクト {name} は既に存在しています。")

    # プロジェクトを削除する
    def remove_project(self, project_name):
        if project_name in self.projects:
            del self.projects[project_name]
        else:
            print(f"プロジェクト {project_name} は存在しません。")

    # タスクを追加する
    def add_task(self, project_name, task):
        if project_name in self.projects:
            self.projects[project_name].append(task)
        else:
            print(f"プロジェクト {project_name} は存在しません。")

    # タスクを削除する
    def remove_task(self, project_name, index):
        if project_name in self.projects:
            try:
                self.projects[project_name].pop(index)
            except IndexError:
                print(f"プロジェクト {project_name} にはインデックス {index} のタスクは存在しません。")
        else:
            print(f"プロジェクト {project_name} は存在しません。")

    # プロジェクトとそのタスクを表示する
    def display_projects(self):
        for project, tasks in self.projects.items():
            print(f"{project}: {tasks}")

