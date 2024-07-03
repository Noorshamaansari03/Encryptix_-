class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.description}"


class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Viewing all tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def complete_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            self.tasks[task_id - 1].completed = True
            print(f"Task {task_id} marked as completed.")
        else:
            print("Invalid task ID.")

    def delete_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            task = self.tasks.pop(task_id - 1)
            print(f"Task deleted: {task.description}")
        else:
            print("Invalid task ID.")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description}|{task.completed}\n")
        print(f"Tasks saved to {filename}")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = []
                for line in file:
                    description, completed = line.strip().split('|')
                    self.tasks.append(Task(description, completed == 'True'))
            print(f"Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"No file named {filename} found.")
