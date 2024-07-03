from todo import ToDo

def print_menu():
    print("\nTo-Do List Application")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Save tasks to file")
    print("6. Load tasks from file")
    print("7. Exit")

def main():
    todo = ToDo()
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            todo.add_task(description)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to complete: "))
            todo.complete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            todo.delete_task(task_id)
        elif choice == '5':
            filename = input("Enter filename to save tasks: ")
            todo.save_tasks(filename)
        elif choice == '6':
            filename = input("Enter filename to load tasks: ")
            todo.load_tasks(filename)
        elif choice == '7':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
