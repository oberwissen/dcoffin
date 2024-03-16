import requests

def send_message(channel_id, token, message):
    data = {"content":message}
    header = {"authorization":token}
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    requests.post(url, data=data, headers=header)