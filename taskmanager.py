from task import Task
from file import file_manager

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.sorted_done_list = []
        self.load_tasks()

    def load_tasks(self):
        try:
            self.tasks = [Task(**task_dict) for task_dict in file_manager.tasks]
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []

    def save_tasks(self):
        try:
            file_manager.tasks = [task.to_dict() for task in self.tasks]
            file_manager.save_tasks()
        except Exception as e:
            print(f"File write error: {e}")

    def sorting_done(self):
        try:
            self.sorted_done_list = sorted(self.tasks, key=lambda x: x.done, reverse=True)
            for i, task in enumerate(self.sorted_done_list, 1):
                print(f'{i}. ' + task.display())
        except Exception as e:
            print(f"Sorting error: {e}")

    def display(self):
        if not self.tasks:
            print("No tasks to display.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f'{i}. ' + task.display())

    def add_task(self, title, description):
        try:
            task = Task(title, description)
            self.tasks.append(task)
            self.save_tasks()
        except Exception as e:
            print(f"Error adding task: {e}")

    def del_task(self, index):
        try:
            index -= 1
            if 0 <= index < len(self.tasks):
                removed = self.tasks.pop(index)
                print(f"Removed: {removed.display()}")
                self.save_tasks()
            else:
                print("Index out of range.")
        except Exception as e:
            print(f"Error deleting task: {e}")

    def done_task(self, index):
        try:
            index -= 1
            if 0 <= index < len(self.tasks):
                self.tasks[index].done_setter()
                self.save_tasks()
            else:
                print("Index out of range.")
        except Exception as e:
            print(f"Error marking task as done: {e}")

    def edit_task(self, index, new_title, new_description):
        try:
            index -= 1
            if 0 <= index < len(self.tasks):
                self.tasks[index].title = new_title
                self.tasks[index].description = new_description
                self.tasks[index].creation_date = Task(new_title, new_description).creation_date
                self.save_tasks()
                print(f"Task {index+1} edited.")
            else:
                print("Index out of range.")
        except Exception as e:
            print(f"Error editing task: {e}")

my_task_manager = TaskManager()

""" if __name__ == "__main__":
    my_task_manager.display()
    print('\n-------------------\ndeleting task 1.\nmarking as done 2.\n-------------------')
    my_task_manager.del_task(1)
    my_task_manager.done_task(2)
    my_task_manager.display() """