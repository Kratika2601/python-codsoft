tasks= []

def add(new):
    tasks.append(new)
    print("new task added to the list.")

def remove(index):
    if 1<=index<=len(tasks):
        tasks.pop(index-1)
        print("Task removed from the list.")
    else:
        print("Invalid task index.")

def view():
    if tasks:
        print("To-Do List:")
        print(*tasks,sep="\n")
    else:
        print("No tasks in the list.")

#MAIN PROGRAM
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Quit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        new = input("Enter the task: ")
        add(new)
    elif choice == '2':
        view()
        index = int(input("Enter the index of the task to remove: "))
        remove(index)
    elif choice == '3':
        view()
    elif choice == '4':
        print("final To-Do-List")
        break
    else:
        print("Invalid choice. Please try again.")
