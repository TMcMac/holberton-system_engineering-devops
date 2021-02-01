#!/usr/bin/python3
"""
Python script that, using https://jsonplaceholder.typicode.com/
for a given employee ID, returns
information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import requests
    import json

    data_user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    json_dict = {}

    for item in data_user:
        emp_id = item['id']
        data_todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(emp_id)).json()
        tasks = []
        for task in data_todos:
            new_item = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": task.get('username')}
            tasks.append(new_item)
        json_dict[emp_id] = tasks

    with open('todo_all_employees.json', mode='w') as new:
        json.dump(json_dict, new)
