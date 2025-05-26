# main
from task import Task
from file import file_manager
from taskmanager import my_task_manager

def show_tasks():
    print("\n--- TASKS ---")
    my_task_manager.display()
    #print('\n-------------------')

def show_sorted_tasks():
    print("\n--- SORTED TASKS ---")
    my_task_manager.sorting_done()
    #print('\n-------------------')

if __name__ == "__main__":
    # Example usage
    #Task("Complete the project", "Finish all modules")
    #Task("Review the code", "Check for bugs")
    #show_tasks()
    #my_task_manager.add_task("Test task", "This is a test.")
    #show_tasks()
    #my_task_manager.done_task(2)
    #my_task_manager.sorting_done()
    #show_tasks()
    #my_task_manager.edit_task(1, "Edited task", "Now with a new description.")
    #show_tasks()
    #my_task_manager.del_task(1)
    show_tasks()
    show_sorted_tasks()
    show_tasks()