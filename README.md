# to_do-list-console


DESCRIPTION:

The to do list application is a command line interface version.


FEATURES AND FUNCTIONALITY:

- The Basic Operations include:
                        - Adding tasks
                        - Displaying tasks
                        - Marking tasks as completed
                        - Removing tasks

- Create a loop that continuosly prompts the user for commands and calls the appropriate funcrions based on the user's input

ADDING TASKS


This code defines a function named add_tasks(). The function allows the user to add a task by taking user input for the task title. It creates a dictionary called task with keys 'title' and 'completed' to store the title and completion status respectively. The tasks.append(task) line adds the task dictionary to the tasks list. Finally, it prints a success message indicating that the task has been added successfully.


DISPLAYING TASKS

This code defines a function named display_tasks(). The function displays the tasks stored in the tasks list. It first prints a header message indicating that it will display the tasks. Then, it uses a for loop along with the enumerate() function to iterate over the tasks list. The enumerate() function provides both the index and the task itself. For each task, it determines the status based on the value of the 'completed' key in the task dictionary. It then prints the task index, title, and status.

