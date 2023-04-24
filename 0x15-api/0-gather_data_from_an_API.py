#!/usr/bin/python3
"""
This script uses a given REST API for employee !D and returns
information about his/her TODO list progress.
"""

if __name__ == '__main__':
    import requests
    import sys

    _id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(_id)

    user = requests.get(user_url)
    user = user.json()

    todos = requests.get(todos_url)
    todos = todos.json()

    task_titles = []
    num_of_done_tasks = 0
    total_num_of_tasks = 0

    for task in todos:
        total_num_of_tasks += 1
        if task.get('completed') == True:
            num_of_done_tasks += 1
            task_titles.append(task.get('title'))

    answer = "Employee {} is done with tasks({}/{}):"
    print(answer.format(user.get('name'), num_of_done_tasks, total_num_of_tasks))

    for task_title in task_titles:
        print("\t {}".format(task_title))
