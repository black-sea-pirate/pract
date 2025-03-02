class Task:

    def __init__(self, title, description = None, completed = False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def __repr__(self):
        tepm = 'Task \"{}\", Completed: {}'.format(self.title, self.completed)
        return repr(tepm)

def add_task(tasks_list, title, description=""):
    if title:
        obj_task = Task(title, description)
        tasks_list.append(obj_task)
    else:
        print("error empty task ")
    return

def mark_task_complete(tasks_list, title):
    for i in range(len(tasks_list)):
        if tasks_list[i].title == title:
            tasks_list[i].mark_complete()
    
tasks = []
add_task(tasks, "gym")
add_task(tasks, "work")
add_task(tasks, "")
add_task(tasks, "life")

mark_task_complete(tasks, "gym")
print(tasks)