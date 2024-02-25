import os
import sys
import threading
import time
import shutil
from zipfile import ZipFile
import io

from DSECTOR import setup
from DSECTOR import clear_terminal
from DSECTOR import set_terminal_title
from DSECTOR import input_text
from DSECTOR import thread_list

debug_enabled = False
debug_request_code = True


from projekt import firmware_over_the_air

from LANG import selected

if debug_enabled == True:
    from OBER import DEBUG as debug
    print("WAITING FOR DEBUGGER")
    debug.init()
    from OBER.DEBUG import log
else:
    def log(mess):
        pass



log("setting terminal title...")
set_terminal_title()
log("successfuly set terminal title")

clear_terminal()

log("importing modules")
try:
    import requests
    import fade
    import colorama
    colorama.init(autoreset=True)
except Exception as e:
    log(f"Exception : {e}")
    print(f"------ {e}")
    print("EN Missing module please install required modules.")
    print("TR Eksik modüller, lütfen gerekli modülleri indirin.")
    exit(1)

log("cheching oobe status")
with open("OBER/is_first_time.txt","r") as is_first_time_file:
    is_first_time = is_first_time_file.read().splitlines()[0]
    if is_first_time == "1":
        log("oobe is active")
        setup()
    else:
        log("oobe is complete")

log("checking language")
with open("OBER/lang.txt", "r") as lang_file:
    selected.selected_lang = lang_file.read().splitlines()[0]
    if selected.selected_lang == "TR":
        log("Language is TR")
        from LANG import turkish as string
    if selected.selected_lang == "EN":
        log("Language is EN")
        from LANG import english as string


def main(opcode = None):
    clear_terminal()
    print(fade.brazil(string.ascii_title))
    if opcode == 0x1:
        log("not_a_option triggered")
        print(string.not_a_option)
    if opcode == 0x2:
        log("spam_started triggered")
        print(string.spam_started)
    print(string.start_menu)
    while True:
        choice = str(input(input_text))
        if len(choice) == 0:
            choice = "`"
        if choice[0] == "0":
            clear_terminal()
            print(string.thanks_and_bye)
            sys.exit(0)
        if choice[0] == "1":
            pass
        if choice[0] == "2":
            normal_spam_frontend()
            break
        if choice[0] == "3":
            changelog()
            break
        clear_terminal()
        main(opcode=0x1)


def changelog():
    clear_terminal()
    print(string.whats_new)
    input(string.enter_to_return)
    main()

def check_for_updates():
    log("Checking for updates")
    print(string.checking_updates)
    try:
        repo_revision = requests.get("https://raw.githubusercontent.com/oberwissen/dcoffin/main/revision.txt").text.splitlines()[0]
    except:
        return
    if int(repo_revision) > firmware_over_the_air.revision:
        print(string.update_available)
        choose = str(input(input_text))
        if choose == "y":
            pass
        else:
            clear_terminal()
            return
        update()

def update():
    clear_terminal()
    print(string.updating)
    with open("OBER/is_first_time.txt", "r") as file:
        is_first_time = file.read()
    with open("discord/tokens.txt", "r") as file:
        tokens = file.read()
    with open("discord/channel_ids.txt", "r") as file:
        channel_ids = file.read()
    with open("OBER/lang.txt", "r") as file:
        lang = file.read()
    remove_all_files()
    package = requests.get("https://github.com/oberwissen/dcoffin/raw/main/ota/sec.zip")
    update_package = ZipFile(io.BytesIO(package.content))
    update_package.extractall(".")
    with open("discord/tokens.txt", "w") as file:
        file.write(tokens)
    with open("discord/channel_ids.txt", "w") as file:
        file.write(channel_ids)
    with open("OBER/is_first_time.txt", "w") as file:
        file.write(is_first_time)
    with open("OBER/lang.txt", "w") as file:
        file.write(lang)
    print(string.update_success)


def remove_all_files():
    for filename in os.listdir("."):
        file_path = os.path.join(".", filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def spam(token, channel_id, message, delay):
    headers = {
        "authorization" : token
    }
    data = {
        "content" : message
    }
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    while True:
        time.sleep(delay)
        request_spam = requests.post(url, headers=headers, data=data)
        code = request_spam.status_code
        if str(code)[0] == 2:
            pass
        if code == 429:
            log(f"Hit ratelimit - retry after :{request_spam.json()['retry_after']}")
            time.sleep(float(request_spam.json()["retry_after"]) + 0.62)
        if code == 401:
            print("\n" + string.invalid_token)
            return
        if code == 403:
            print("\n" + string.access_denied)
        if debug_request_code == True:
            log(str(code))


def start_spam(message,delay):
    tokens = open("discord/tokens.txt", "r").read().splitlines()
    channel_ids = open("discord/channel_ids.txt", "r").read().splitlines()
    for token in tokens:
        for channel_id in channel_ids:
            thread = threading.Thread(target=spam, args=(token, channel_id, message, delay), daemon=True)
            thread.start()
            thread_list.append(thread)
            main(0x2)



def normal_spam_frontend():
    clear_terminal()
    print(string.spam_tutorial)
    input()
    clear_terminal()
    while True:
        message = input(string.message)
        if len(message) != 0:
            clear_terminal()
            break
        print(string.empty_message_error, end="\n\n")
    while True:
        try:
            delay = float(input(string.delay))
            break
        except ValueError:
            print(string.please_enter_valid_num, end="\n\n")
    start_spam(message, delay)




if __name__ == '__main__':
    check_for_updates()
    main()
else:
    print(string.cant_import_module)
    sys.exit()




