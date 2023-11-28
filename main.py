from taskClass import Task
from taskManegerClass import ProjectManager
import re

pm = ProjectManager()

def viewPjList():
    for pjList in pm.projects.keys():
        print(pjList)

def viewTaskList():
    for tList in pm.projects.values():
        print(tList)

while True:
    selectMode = int(input("0:DictView 1:pjAdd 2:pjDel 3:taskAdd 4:taskDel 5:changeStatus 6:end >> "))

    if selectMode == 0:
        pm.display_projects()

    elif selectMode == 1:
        # pm.add_project("pj1")
        pm.add_project(input("addするpj名を入力 >> "))

    elif selectMode == 2:
        viewPjList()
        pm.remove_project(input("removeするpj名を入力 >> "))

    elif selectMode == 3:
        viewPjList()
        pjName = input("追加したいプロジェクト名を入力 >> ")
        while True:
            if not(pjName in pm.projects):
                pjName = input("追加したいプロジェクト名を入力 >> ")
            else:
                break

        addContent = input("追加したいタスク内容を入力 >> ")
        while True:
            addDate = input("期日を入力(YYYY-MM-DD形式) >> ")
            if re.match(r"^\d{4}-\d{2}-\d{2}$", addDate):
                break
            else:
                print("入力形式が正しくありません。再度入力してください。")

        addManeger = input("担当者名を記入>> ")
        task = Task(addContent,addDate,addManeger)
        rDay = task.calcRemainingDays()
        pm.add_task(pjName, task)
        print(f"残り日数：{rDay}日")

    elif selectMode == 4:
        viewPjList()
        pjName = input("削除したいpj名を入力 >> ")
        delTaskIndex = int(input("削除したtask番号を入力 >> "))
        pm.remove_task(pjName, delTaskIndex)

    elif selectMode == 5:
        viewPjList()
        pjName = input("変更するタスクが入っているプロジェクト名を入力 >> ")
        while True:
            if not(pjName in pm.projects):
                pjName = input("変更するタスクが入っているプロジェクト名を入力 >> ")
            else:
                break

        num = int(input("何番目のタスク？ >>"))
        status = input("変更するステータス >>")
        pm.projects[pjName][num].statusChange(status)

    elif selectMode == 6:
        break

    pm.display_projects()

