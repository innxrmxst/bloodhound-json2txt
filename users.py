#!/usr/bin/python
#encoding=utf8

import sys
import json

if len(sys.argv) == 1:
    print("Usage: " + sys.argv[0] + " bloodhound_users.json")
    sys.exit()

bhuserfile = sys.argv[1]
with open(bhuserfile) as data_file:
    data = json.load(data_file)

print(data['data'][0]['Properties'])
#print("name,enabled,displayname,email,title,description")
for i in data['data']:
    oname = i['Properties']['name'] 
    print("{}".format(oname))
