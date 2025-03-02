
class Task:
    # конструктор класу
    # визначає атрибути title, description, completed
    def __init__(self, title, desc='', completed=False):
        self.title = title
        self.description = desc
        self.completed = completed

    # змінює стан атрибуту completed на True 
    def mark_completed(self):
        self.completed = True

    # опис об'єкта
    # по суті при виводі об'єкта через print() повертає наступне:
    # <Task: "Єбаніє Осла", Completed: True>
    def __repr__(self):
        temp = '<Task: \"{}\", Completed: {}>'.format(self.title, self.completed)
        return repr(temp)

######
######

# якщо ім'я таски вказано, то вона додається в кінець списку
# якщо ні - еррор
def add_task(tasks_list, title='', description=''):
    if(title!=''):
        task = Task(title, description)
        tasks_list.append(task)
        print('> Task ', title, ' succesfully added')
    else:
        print(">> ERROR! Не вказано назву задачі!")

# використовуємо цикл for з ітератором taskNumber
# який по дефолту 0 і збільшується з кожною ітерацією
#
# всього в циклі ітерацій стільки ж, скільки елементів у списку
# бо в range вказано довжину переданого в параметрах списку
#
# як тільки таска з потрібним значенням знайдена, 
# return виходить з функції до виведення еррора. 
# Якщо цього не сталося - еррор буде виведено

def mark_task_complete(tasks_list, title):
    for taskNumber in range(len(tasks_list)):
        if tasks_list[taskNumber].title == title:
            tasks_list[taskNumber].mark_completed()
            print('> Task ', title, ' marked as complete')
            return
    
    print(">> ERROR! Задачу з таким іменем не знайдено!")


# список
tasks = []

print('\n\n-- Додаємо таски --')
add_task(tasks,'chistit_hui','прийняти ванну')
add_task(tasks,'drochka','подоїти коня')
add_task(tasks,'genocid_rusni','винести сміття')

add_task(tasks,'','якщо це виведе в термінал то ти підор')
add_task(tasks,'sasai_kudasai')

print('\n', tasks)

print('\n\n-- Завершуємо виконання --')
mark_task_complete(tasks,'drochka')
mark_task_complete(tasks,'chistit_hui')
mark_task_complete(tasks,'error')

print('\n', tasks)
