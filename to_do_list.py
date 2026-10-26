print("\n---Welcome to 'To DO List'---")

tasks = []

def add():
    task = (input("Enter Your Task:"))
    tasks.append(task)
    print("Task Added to List Successfuly")

def view():
    if not tasks:
        print("NO Tasks Added or All tasks Completed")
    else:
        for number, task in enumerate(tasks, start =1):
            print(f"\n{number}.{task}")

def remove():
    view()
    if tasks:
        try:
            number = int(input("Enter Task Number To Remove:"))
        except ValueError:
            print("Please Enter a valid Number")
            return
        if(1 <= number <= len(tasks)):
            tasks.pop(number - 1)
            print("Task Removed. List updated Successfully")
        else:
            print("Invalid Task Number")

def exit_app():
    print("Thanks For Using The List. \nSee Yeah !")

def func():
    options = {'1': add,
                   '2': view,
                   '3': remove,
                   '4': exit_app
                }

    while True:
        print("\n1: Add Task")
        print("2: View Tasks")
        print("3: Remove Task")
        print("4: Exit")

        choice = input("Enter your Choice :")

        if choice in options:
            options[choice]()
            if choice == '4':
                break
        else:
                print("Invalid Choice")

func()


        
