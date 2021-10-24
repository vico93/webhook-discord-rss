#!/usr/bin/env python3

import json


print("Nome do Feed:")
key = input()

print("Nome do Webhook:")
username = input()

print("URL do RSS:")
rss_url = input()

print("URL do Webhook:")
url_webhook = input()

print("URL do avatar do Webhook:")
url_avatar = input()

guid ="/root/rss-discord/GUID/" + key + ".guid"

with open("/root/rss-discord/db.json", "r") as json_file:
    DICO = json.load(json_file)


DICO["URL"][key] = rss_url
DICO["WEBHOOK"][key] = url_webhook
DICO["USERNAME"][key] = username
DICO["AVATAR"][key] = url_avatar
DICO["GUID"][key] = guid

print(json.dumps(DICO, sort_keys=True, indent=4))

with open('/root/rss-discord/db.json', 'w') as f:
    f.write(json.dumps(DICO, sort_keys=True, indent=4))
f.close()
