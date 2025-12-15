# Import other modules needed for this file to work.
import storage                 # To interact with the database.
from datetime import date      # To get the current date when a task is completed.
from colorama import Fore, Style # To add color to the text output.

def _get_next_id(tasks):
    """
    A helper function (indicated by the '_' at the start) to get a unique ID for a new task.
    """
    # If there are no tasks, start with ID 1.
    if not tasks:
        return 1
    # Otherwise, find the biggest ID in the current list and add 1 to it.
    return max(task['id'] for task in tasks) + 1

def _find_task_by_id(tasks, task_id):
    """A helper function to find a specific task in the list using its ID."""
    # Loop through every task in the list.
    for task in tasks:
        # If the task's ID matches the one we're looking for...
        if task['id'] == task_id:
            return task # ...return that task.
    return None # Return None if no task with the given ID is found.

def _print_task_summary(tasks):
    """Helper function to print a summarized list of tasks (ID and title)."""
    print("\n--- Your Tasks ---")
    # If the list is empty, just say so.
    if not tasks:
        print("No tasks to display.")
        return
    # Loop through the tasks (sorted by ID) and print a simple line for each.
    for task in sorted(tasks, key=lambda t: t['id']):
        print(f"  [{task['id']}] {task['title']}")
    print("-" * 20)

def add_task(tasks):
    """
    Adds a new task to the list.

    It asks the user for details, creates a new task, and saves it to the database.
    """
    print("\n--- Add a New Task ---")
    # Ask the user for the task's title. This is required.
    title = input("Enter task title (required): ")
    if not title:
        print(Fore.RED + "Error: Title cannot be empty.")
        return tasks # Return original list if there's an error

    # Ask for optional details.
    description = input("Enter task description (optional): ")
    priority = input("Enter priority (Low, Medium, High) (optional): ").capitalize()
    due_date = input("Enter due date (e.g., tomorrow, 2025-07-15) (optional): ")

    # A dictionary is like a container for storing related pieces of information.
    # Here, we create a dictionary to hold all the details of the new task.
    new_task = {
        "id": _get_next_id(tasks), # Get a new, unique ID.
        "title": title,
        "description": description,
        # If the user entered a valid priority, use it. Otherwise, default to "Medium".
        "priority": priority if priority in ["Low", "Medium", "High"] else "Medium",
        "done": False, # A new task is never done.
        "due_date": due_date,
        "completion_date": "" # Will be set when the task is marked as done.
    }

    storage.add_task_db(new_task) # Save the new task to the database.
    print(Fore.GREEN + f"Success: Task '{title}' added.")
    return storage.load_tasks() # Return the fresh list from the DB
    
def list_tasks(tasks, status_filter=None):
    """
    Displays all tasks.

    Shows the ID, title, and completion status for each task.

    Args:
        tasks (list): The list of task dictionaries.
        status_filter (str, optional): "done" or "not_done" to filter tasks.
                                       Defaults to None (show all).
    """
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks found.")
        return

    # By default, we display all tasks.
    tasks_to_display = tasks
    # But if a filter was provided (like "done" or "not_done")...
    if status_filter == "done":
        # ...we create a new list containing only the tasks that are done.
        tasks_to_display = [task for task in tasks if task['done']]
    elif status_filter == "not_done":
        # ...or a new list containing only the tasks that are NOT done.
        tasks_to_display = [task for task in tasks if not task['done']]

    # Sort the list so that "Not Done" tasks appear before "Done" tasks.
    sorted_tasks = sorted(tasks_to_display, key=lambda t: t['done'])

    # Loop through each task in the list we are displaying.
    for task in sorted_tasks:
        print("-" * 25) # Print a line to separate tasks.
        # Print the task's ID and title in bold.
        print(f"{Style.BRIGHT}[{task['id']}] {task['title']}{Style.RESET_ALL}")
        
        # Display Description and Priority
        # .get('description') safely gets the description. If it doesn't exist, it won't crash.
        # 'or 'N/A'' means if the description is empty, we print 'N/A' instead.
        print(f"  {Fore.CYAN}{'Desc:':<10}{Style.RESET_ALL}{task.get('description') or 'N/A'}") # '<10' pads the text to 10 characters.
        print(f"  {Fore.CYAN}{'Priority:':<10}{Style.RESET_ALL}{task.get('priority')}")

        # Set the status text and color based on whether the task is done.
        status = f"{Fore.GREEN}Done{Style.RESET_ALL}" if task['done'] else f"{Fore.YELLOW}Not Done{Style.RESET_ALL}"
        
        # Check if the task is done and has a completion date.
        if task['done'] and task.get('completion_date'):
            date_info = f"{Fore.BLUE}on {task['completion_date']}{Style.RESET_ALL}"
            print(f"  {Fore.CYAN}{'Status:':<10}{Style.RESET_ALL}{status} {date_info}")
        # Check if the task is not done and has a due date.
        elif not task['done'] and task.get('due_date'):
            date_info = f"{Fore.MAGENTA}due: {task['due_date']}{Style.RESET_ALL}"
            print(f"  {Fore.CYAN}{'Status:':<10}{Style.RESET_ALL}{status} ({date_info})")
        else:
            # If neither of the above, just print the status.
            print(f"  {Fore.CYAN}{'Status:':<10}{Style.RESET_ALL}{status}")
    print("-" * 25) # Final separator

def toggle_task_status(tasks):
    """
    Changes a task's status from 'Done' to 'Not Done', or vice-versa.
    """
    print("\n--- Mark Task Complete / Incomplete ---")
    _print_task_summary(tasks) # Show the user a list of tasks to choose from.
    try:
        task_id = int(input("Enter the ID of the task to toggle: "))
    except ValueError:
        print(Fore.RED + "Error: Invalid ID. Please enter a number.")
        return tasks # Exit the function if the user didn't enter a valid number.

    task = _find_task_by_id(tasks, task_id)
    if task:
        # Flip the boolean 'done' status.
        task['done'] = not task['done']

        # If the task is now done, record the completion date.
        if task['done']:
            task['completion_date'] = date.today().strftime("%Y-%m-%d") # Format: YYYY-MM-DD
        else:
            # If it's toggled back to not done, clear the completion date.
            task['completion_date'] = ""

        storage.update_task_db(task) # Save this change to the database.
        new_status = "Done" if task['done'] else "Not Done"
        print(Fore.GREEN + f"Success: Task '{task['title']}' marked as {new_status}.")
    else:
        print(Fore.RED + "Error: Task ID not found.")
    
    return storage.load_tasks() # Return the fresh list from the DB

def update_task(tasks):
    """
    Updates an existing task's title, description, or priority.
    """
    print("\n--- Update a Task ---")
    _print_task_summary(tasks) # Show the list of tasks.
    try:
        task_id = int(input("Enter the ID of the task to update: "))
    except ValueError:
        print(Fore.RED + "Error: Invalid ID. Please enter a number.")
        return tasks

    task = _find_task_by_id(tasks, task_id)
    if not task:
        print(Fore.RED + "Error: Task ID not found.")
        return tasks

    print(f"Updating task: '{task['title']}'")
    
    # Ask for new values. If the user just presses Enter, the old value is kept.
    new_title = input(f"Enter new title (current: '{task['title']}') or press Enter to keep: ")
    if new_title:
        task['title'] = new_title

    new_description = input(f"Enter new description (current: '{task['description']}') or press Enter to keep: ")
    if new_description:
        task['description'] = new_description

    new_priority = input(f"Enter new priority (current: '{task['priority']}') or press Enter to keep: ").capitalize()
    if new_priority in ["Low", "Medium", "High"]:
        task['priority'] = new_priority
    
    storage.update_task_db(task) # Save the updated task to the database.
    print(Fore.GREEN + f"Success: Task {task_id} updated.")
    return storage.load_tasks() # Return the fresh list from the DB

def delete_task(tasks):
    """
    Deletes a task from the list.
    """
    print("\n--- Delete a Task ---")
    _print_task_summary(tasks) # Show the list of tasks.
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
    except ValueError:
        print(Fore.RED + "Error: Invalid ID. Please enter a number.")
        return tasks

    task = _find_task_by_id(tasks, task_id)
    if not task:
        print(Fore.RED + "Error: Task ID not found.")
        return tasks

    task_title = task['title'] # Save the title so we can use it in the success message.
    storage.delete_task_db(task_id) # Delete the task from the database.
    print(Fore.GREEN + f"Success: Task '{task_title}' deleted.")
    return storage.load_tasks() # Return the fresh list from the DB

def search_tasks(tasks):
    """
    Searches for tasks containing a specific keyword in their title or description.
    """
    print("\n--- Search Tasks ---")
    keyword = input("Enter keyword to search for: ").lower()
    if not keyword:
        print(Fore.RED + "Error: Search keyword cannot be empty.")
        return

    # This is a list comprehension. It's a short way to build a list.
    # It creates a new list 'found_tasks' containing every task where the keyword
    # appears in its title or description (converted to lowercase for a case-insensitive search).
    found_tasks = [
        task for task in tasks
        if keyword in task['title'].lower() or keyword in task['description'].lower()
    ]

    if not found_tasks:
        print(Fore.YELLOW + f"No tasks found with keyword: '{keyword}'")
    else:
        print(Fore.GREEN + f"Found {len(found_tasks)} task(s) with keyword: '{keyword}'")
        list_tasks(found_tasks) # Reuse our existing list_tasks function to print the results.
