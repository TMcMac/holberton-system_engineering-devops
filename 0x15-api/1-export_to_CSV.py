#!/usr/bin/python3
"""
Python script that, using https://jsonplaceholder.typicode.com/
for a given employee ID, returns
information about his/her TODO list progress.
"""

import csv
import requests
import json
from sys import argv

employee_id = argv[1]
data_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(employee_id)).json()
data_todos = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId={}'
    .format(employee_id)).json()

with open(str(employee_id) + '.csv', mode='w') as employee_tasks:
    employee_writer = csv.writer(employee_tasks,
                                 delimiter=',',
                                 quotechar='"',
                                 quoting=csv.QUOTE_ALL)

    for task in data_todos:
        employee_writer.writerow([task.get('userId'),
                                  data_user.get('username'),
                                  task.get('completed'),
                                  task.get('title')])
