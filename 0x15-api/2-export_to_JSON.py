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
    tod = tod.json()
    tskList = []
    todou = {}
    for i in tod:
        if i.get('userId') == int(uid):
            dict = {"task": i.get('title'),
                    "completed": i.get('completed'),
                    "username": url.json().get('username')}
            tskList.append(dict)
    todou[uid] = tskList
    fileName = "{}.json".format(uid)
    with open(fileName, mode='w') as jsn:
        json.dump(todou, jsn)
