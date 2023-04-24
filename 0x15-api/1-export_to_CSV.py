#!/usr/bin/python3
"""
This script export data gotten from a given Rest API
in the CSV (Comma Seperated Values) format.
"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    _id = sys.argv[1]
    url1 = "https://jsonplaceholder.typicode.com/"
    url2 = "users/{}?_embed=todos".format(user_id)
    url = "{}{}".format(url1, url2)

    resp = requests.get(url)
    json_resp = resp.text
    dict_resp = json.loads(json_resp)
    username = dict_resp.get('username')
    todos = dict_resp.get('todos')

    records = ''
    csv_temp = '{},{},{},{}{}'
    for task in todos:
        _user_id = '"{}"'.format(user_id)
        _username = '"{}"'.format(username)
        _completed = '"{}"'.format(task.get('completed'))
        _title = '"{}"'.format(task.get('title'))
        _row = [_user_id, _username, _completed, _title, '\n']
        records += csv_temp.format(*_row)

    with open('{}.csv'.format(user_id), 'w') as f:
        f.write(records)
