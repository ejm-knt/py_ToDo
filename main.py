from taskClass import Task
from taskManegerClass import ProjectManager

pm = ProjectManager()

while True:
    selectMode = int(input("0:DictView 1:pjAdd 2:pjDel 3:taskAdd 4:taskDel 5:end >> "))

    if selectMode == 0:
        pm.display_projects()

    elif selectMode == 1:
        # pm.add_project("pj1")
        pm.add_project(input("addするpj名を入力 >> "))

    elif selectMode == 2:
        pm.remove_project(input("removeするpj名を入力 >> "))

    elif selectMode == 3:
        pjName = input("追加したいプロジェクト名を入力 >> ")
        addContent = input("追加したいタスク内容を入力 >> ")
        addDate = input("期日を入力(YYYY-MM-DD形式) >> ")
        addManeger = input("担当者名を記入>> ")
        task = Task(addContent,addDate,addManeger)
        rDay = task.calcRemainingDays()
        pm.add_task(pjName, task)
        print(f"残り日数：{rDay}日")

    elif selectMode == 4:
        pjName = input("削除したいpj名を入力 >> ")
        for tList in pm.projects[pjName]:
            print(tList)
        delTaskIndex = int(input("削除したtask番号を入力 >> "))
        pm.remove_task(pjName, delTaskIndex)

    elif selectMode == 5:
        break

    pm.display_projects()