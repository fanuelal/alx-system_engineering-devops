#!/usr/bin/python3
"""script to export data in the CSV format"""


import requests
import json
import sys
import csv
if __name__ == "__main__":

    uid = sys.argv[1]
    url = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(uid))
    name = url.json().get('username')
    tod = requests.get('https://jsonplaceholder.typicode.com/todos')
    totaltasks = 0
    completed = 0
    fileName = "{}.csv".format(uid)
    with open(fileName, 'w') as csvfile:
        obj = csv.writer(csvfile, delimiter=',', quotechar='"',
                         quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in tod.json():
            if task.get('userId') == int(uid):
                obj.writerow([uid, name,
                              str(task.get('completed')), task.get('title')])
