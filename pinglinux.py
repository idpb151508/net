import subprocess
from time import sleep
import requests

ip = "192.168.1.6"

def notifyNetwork(message):
    token = ""
    uri = "https://notify-api.line.me/api/notify"
    header = {"Authorization": "Bearer "+token}
    msg = {"message": message}
    resp = requests.post(uri, headers=header, data=msg)


def ping():
    try:
        subprocess.check_output(["ping", "-c", "1", ip])
        return True
    except subprocess.CalledProcessError:
        return False

previusStatus = True
while True:
    currentStatus = ping()  
    if currentStatus == previusStatus:
        print('-----no notify--------')
    else:
        if currentStatus:
            statusNetwork = 'UP'
            message = f"{ip} {statusNetwork}"
            notifyNetwork(message)
            print('--- Notify ----')
        else:
            statusNetwork = 'DOWN'
            message = f"{ip} {statusNetwork}"
            notifyNetwork(message)
            print('--- Notify ----')
    previusStatus = currentStatus
    print(currentStatus)
    sleep(2)
