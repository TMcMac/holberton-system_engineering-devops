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
data_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(employee_id)).json()
data_todos = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId={}'
    .format(employee_id)).json()

tasks = []
json_dict = {}

for task in data_todos:
    new_item = {"task": task.get('title'),
                "completed": task.get('completed'),
                "username": data_user.get('username')}
    tasks.append(new_item)

json_dict = {argv[1]: tasks}

with open(str(employee_id) + '.json', mode='w') as new_json:
    json.dump(json_dict, new_json)
