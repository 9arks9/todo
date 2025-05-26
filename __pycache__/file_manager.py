import json
import task

#x = task.t_list

filename = 'my_tasks.json' 

class File_manager:
    def __init__(self,tasks = []):
       # self.tasks = x
        self.load_tasks(filename)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Creating a new file.")
            with open(filename, 'w') as file:
                json.dump([], file)
            self.tasks = []
            print("New file has been created.")
        except json.JSONDecodeError:
            print("File read error. The file may be corrupted.")
            self.tasks = []
    
    def save_tasks(self):
        try:
            with open(filename, 'w') as file:
                json.dump(self.tasks, file, indent=4)
                print('*[Task] saved successfully.')
        except IOError as e:
            print(f"File write error: {e}")

    def remove_task(self,index):
        index = int(index)
        index -= 1  # Adjusting for 0-based index
        if index < 0 or index >= len(task.Task.t_list):
            print(f"[Task] Index {index-1} is out of range.")
            return
        removed_task = task.Task.t_list.pop(index)
        self.save_tasks()
        print(f"[Task] '{removed_task}' removed.")
    




