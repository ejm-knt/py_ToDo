from math import ceil
from datetime import datetime

# タスククラスの定義
class Task:
    """
    TaskClass_引数:
    content (str): タスクの内容
    deadLineTaskDate (str): タスクの期日。形式は 'yyyy-mm-dd'
    manegerName (str): タスクの担当者名
    """

    def __init__(self, content, deadLineTaskDate, manegerName, taskStatus="ToDo"):
        self.content = content                      # タスクの内容
        self.createTaskDate = datetime.now()        # タスク作成時刻
        self.deadLineTaskDate = datetime.strptime(deadLineTaskDate, '%Y-%m-%d') #タスク期日
        self.manegerName = manegerName              # タスク担当者
        self.taskStatus = taskStatus                # タスクの進捗状態
        self.taskComment = {}                       # タスクに対するコメント

    def __repr__(self):
        """print関数で表示させる関数"""
        return f'Task(content={self.content},CTDate={self.createTaskDate},DLTDate={self.deadLineTaskDate},manegerName={self.manegerName},taskStatus={self.taskStatus},taskComment={self.taskComment})'

    def calcRemainingDays(self):
        """残日数 = 期日 -  作成日"""
        delta = self.deadLineTaskDate - self.createTaskDate
        delta_in_minutes = delta.total_seconds() / 60
        if delta_in_minutes < 0:
            return 0
        else:    
            return ceil(delta_in_minutes / (24 * 60))  # 分を日数に変換

    def statusChange(self, taskStatus):
        """Statusは下記を格納すること\n
        "ToDo":"未着手"\n
        "Doing":"進行中"\n
        "Done":"完了"\n
        "Pending":"保留"\n
        "Cancel":"中止" """
        statusesList = ["ToDo", "Doing", "Done", "Pending", "Cancel"]
        if taskStatus not in statusesList:
            return f"無効なstatus: {taskStatus}. 次のいずれかを使用してください: {statusesList}"
        else:
            self.taskStatus = taskStatus

    def addComment(self, comment):
        """コメント追加機能。ナンバリングが変わらず更新し続ける"""
        taskCount = 0  #* 使用されていない最小の番号を見つける
        while f"#{taskCount}" in self.taskComment:
            taskCount += 1
        self.taskComment[f"#{taskCount}"] = comment #* コメントを追加する

    def removeComment(self, commentNum):
        """コメント削除機能。キーごと削除する"""
        key = f"#{commentNum}"
        if key in self.taskComment:
            del self.taskComment[key]
        else:
            return f"{key}というコメントは存在していません"
