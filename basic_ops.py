#!/usr/bin/python3
tasks = [] # A Global Variable

def add_tasks():
    global tasks
    #The function takes user input and adds a task
    #to a list.

    title = input("Enter the task to commit to: ")
    task = {'title': title, 'completed': False}
    tasks.append(task)
    print("Task added successfully")


def display_tasks():
    #The function iterates over a list and prints each task
    
    print("Your Tasks include: ")
    for index, task in enumerate(tasks):
        status = "completed" if task['complete'] else "Not Completed"
        print(f"{index + 1}. {task['title'] - status}")
