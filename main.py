import sqlite3


def add_tasks_to_db(tasks):
    db = sqlite3.connect("ToDoList")
    cursor = db.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Tasks(id INTEGER PRIMARY KEY, task TEXT, priority INTEGER)
                ''')
    cursor.executemany(
        ''' INSERT INTO Tasks(task, priority) VALUES(?, ?)''', tasks,)
    db.commit()
    db.close()


def add_tasks():
    tasks = []
    while True:
        task = input(
            "Please add a task to the To Do List (enter 'end' to finish): ")
        if task == "end":
            break
        tasks.append((task, 0,))

    add_tasks_to_db(tasks)


def get_tasks():
    db = sqlite3.connect("ToDoList")
    cursor = db.cursor()
    cursor.execute('''
                   SELECT * FROM Tasks''')
    tasks = cursor.fetchall()
    db.commit()
    db.close()
    return tasks


def update_priorities(id, priority):
    db = sqlite3.connect("ToDoList")
    cursor = db.cursor()
    cursor.execute('''UPDATE Tasks SET priority = ? WHERE id = ?
                   ''', (priority, id))
    db.commit()
    db.close()


def prioritise():
    tasks = get_tasks()
    n = len(tasks)
    priority = [0] * n
    print("Choose which tasks are more important:")
    for i in range(n):
        for j in range(i + 1, n):
            print("A: " + tasks[i][1])
            print("B: " + tasks[j][1])
            choice = input('A or B: ')
            if choice == "A":
                priority[i] = priority[i] + 1
            else:
                priority[j] = priority[j] + 1

    for i in range(n):
        update_priorities(tasks[i][0], priority[i])


def main():
    text = ''' 
    1. Add tasks 
    2. Prioritise tasks
    3. View tasks
    '''
    choice = input(text)
    if choice == "1":
        add_tasks()
    elif choice == "2":
        prioritise()


main()
