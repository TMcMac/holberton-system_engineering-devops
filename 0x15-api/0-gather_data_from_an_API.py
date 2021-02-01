#!/usr/bin/python3
"""
Python script that, using https://jsonplaceholder.typicode.com/
for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
import json
from sys import argv

employee_id = argv[1]
data_users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                          format(employee_id))
data_todos = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId={}'
    .format(employee_id))
user_dict = data_users.json()
todo_dict = data_todos.json()
employee_name = user_dict['name']
done_tasks = []
completed = 0
total_tasks = 0


for done in todo_dict:
    if done.get('completed') is True:
        completed += 1
        done_tasks.append(done.get('title'))
    total_tasks += 1
print("Employee {} is done with tasks({}/{}:)".format(employee_name,
                                                      completed,
                                                      total_tasks))
for task in done_tasks:
    print("\t{}".format(task))
