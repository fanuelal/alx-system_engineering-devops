#!/usr/bin/python3
"""apiis REST API, for a given employee ID,
returns information about his/her TODO list"""


import requests
import json
import sys
if __name__ == "__main__":

    id = sys.argv[1]
    url = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(id))
    name = url.json().get('name')
    tod = requests.get('https://jsonplaceholder.typicode.com/todos')
    totaltasks = 0
    completed = 0
    for i in tod.json():
        if i.get('userId') == int(id):
            totaltasks += 1
            if i.get('completed'):
                completed += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totaltasks))
    print('\n'.join(["\t " + task.get('title') for task in tod.json()
          if task.get('userId') == int(id) and task.get('completed')]))
