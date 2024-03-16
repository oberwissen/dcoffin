import requests

def return_account_info(token):
    info_dict = {}
    url = "https://discord.com/api/v9/users/@me"
    header = { "authorization" : token }
    data = requests.get(url, headers=header)
    if data.status_code != 200:
        return False
    info = data.json()
    info_dict["id"] = info["id"]
    info_dict["username"] = info["username"]
    info_dict["display_name"] = info["global_name"]
    info_dict["2fa"] = info["mfa_enabled"]
    info_dict["email_verified"] = info["verified"]
    info_dict["phone_number"] = info["phone"]
    info_dict["email"] = info["email"]
    return info_dict


