import sys

import requests
import time


def check_token(token):
    time.sleep(1)
    header = {"authorization" : token}
    account = requests.get("https://discord.com/api/v9/users/@me", headers=header)
    if account.status_code == 200:
        return True
    else:
        return False

