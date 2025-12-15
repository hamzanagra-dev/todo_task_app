# Import the other Python files (modules) that contain related code.
import storage  # This module handles saving and loading tasks to the database.
import tasks    # This module contains all the functions for managing tasks (add, delete, etc.).

# Import tools from the 'colorama' library to add color to the text.
from colorama import Fore, Style, init

def print_list_submenu():
    """Prints the submenu for listing and searching tasks."""
    print(f"\n{Style.BRIGHT}--- List/Search Menu ---{Style.RESET_ALL}")
    # Print the available options for the user.
    print("1. Show all tasks")
    print("2. Show pending tasks")
    print("3. Show completed tasks")
    print("4. Search tasks by keyword")
    print(f"0. {Fore.YELLOW}Back to main menu{Style.RESET_ALL}")
    print("-" * 24)

def handle_list_menu(task_list):
    """Handles the logic for the list/search submenu."""
    # This loop keeps showing the menu until the user chooses to go back.
    while True:
        print_list_submenu()
        choice = input("Choose a list/search option: ")

        # Check what the user chose and call the correct function.
        if choice == '1':
            tasks.list_tasks(task_list)  # Show all
        elif choice == '2':
            tasks.list_tasks(task_list, status_filter="not_done")  # Show pending
        elif choice == '3':
            tasks.list_tasks(task_list, status_filter="done")  # Show completed
        elif choice == '4':
            tasks.search_tasks(task_list)
        elif choice == '0':
            return  # 'return' exits this function and goes back to the main menu.
        else:
            # If the user enters something invalid, show an error message.
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
        
        # Pause the program and wait for the user to press Enter.
        input("\nPress Enter to return to the list/search menu...")

def print_menu():
    """Prints the main menu of the application."""
    # The text is styled with colors to make it look better.
    print("\n" + Fore.CYAN + "="*20)
    print(f"=== {Style.BRIGHT}TODO APP by Hamza.arhad{Style.NORMAL} ===")
    print("="*20 + Style.RESET_ALL)
    # Print the main options.
    print("1. Add task") 
    print("2. List / Search tasks")
    print("3. Mark task complete / incomplete")
    print("4. Update task")
    print("5. Delete task")
    print(f"0. {Fore.YELLOW}Exit{Style.RESET_ALL}")
    print(Fore.CYAN + "="*20 + Style.RESET_ALL)

def process_user_choice(choice, task_list):
    """
    Takes the user's choice and the current task list, and calls the appropriate function.
    Returns the potentially updated task list.
    """
    if choice == '1':
        return tasks.add_task(task_list)
    elif choice == '2':
        handle_list_menu(task_list)
        return task_list  # handle_list_menu does not modify the list
    elif choice == '3':
        return tasks.toggle_task_status(task_list)
    elif choice == '4':
        return tasks.update_task(task_list)
    elif choice == '5':
        return tasks.delete_task(task_list)
    else:
        print(Fore.RED + "Invalid choice. Please choose a valid option from the menu.")
        return task_list

def main():
    """Main function to run the To-Do application."""
    # Initialize colorama to automatically reset style after each print.
    init(autoreset=True)
    storage.init_db() # Initialize the database and create the table.
    # Load existing tasks from the file when the application starts.
    task_list = storage.load_tasks()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '0':
            print(Fore.GREEN + "Exiting application. Your tasks are saved.")
            break # Exit the while loop.
        
        # Process the choice and get the updated list
        task_list = process_user_choice(choice, task_list)

        # Add a small pause for better user experience, but not after the list menu
        if choice != '2':
            input("\nPress Enter to return to the menu...")


# This is a standard Python construct.
# It checks if the script is being run directly (not imported).
# If it is, it calls the main() function.
if __name__ == "__main__":
    main()