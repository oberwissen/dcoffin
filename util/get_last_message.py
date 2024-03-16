import requests


def get_latest_message(channel_id, token):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    header = {
        "authorization" : token
    }
    data = requests.get(url, headers=header)
    return data.json()[0]["content"]



