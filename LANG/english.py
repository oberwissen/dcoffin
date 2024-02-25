from colorama import Fore, Style

from projekt import general


langpac_revision = "1"

ascii_title = """
     MADE BY OBERWISSENFÜHRER YAKUP ASLANTAS
██████╗  ██████╗ ██████╗ ███████╗███████╗██╗███╗   ██╗
██╔══██╗██╔════╝██╔═══██╗██╔════╝██╔════╝██║████╗  ██║
██║  ██║██║     ██║   ██║█████╗  █████╗  ██║██╔██╗ ██║
██║  ██║██║     ██║   ██║██╔══╝  ██╔══╝  ██║██║╚██╗██║
██████╔╝╚██████╗╚██████╔╝██║     ██║     ██║██║ ╚████║
╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═══╝
                     OBERWISSEN
                   t.me/oberwissen
"""

cmd_title = f"dcoffin {general.version} - EN {langpac_revision} - t.me/oberwissen"

not_a_option = f"{Fore.RED}{Style.BRIGHT} [ ! ] {Style.RESET_ALL} That option does not exists."
thanks_and_bye = "Thank you for using our product! - t.me/oberwissen"
update_available = "a new update is available, would you like to update? ( y = yes / n = no )"
restart_text = "Restarting..."
spam_tutorial = """
1. Take your token and put it to discord/tokens.txt ( if you want to put more than 1 token just move to new line )
2. Copy the target channels ID and put it to discord/channel_ids.txt ( if you want to put more than 1 channel id just move to new line )

Press [ ENTER ] to continue.
"""
message = "Message : "
delay = "Delay : "
spam_started = "Spam is started, if something goes wrong you will be informed."
cant_import_module = "This tool is not designed to use as a module."
empty_message_error = "Plase enter a message."
please_enter_valid_num = "Please enter a valid number."
invalid_token = "Invalid token"
no_access = "Access denied."
checking_updates = "Checking for updates..."
updating = "Updating... Please wait"
update_success = "Update is successful, restart for it to take effect."
enter_to_return = "Press [ ENTER ] key to return"

whats_new = """
dcoffin version 0.0.1 ----------

 - Initial release
"""


start_menu = f"""
SELECT A OPTION

    --------------- DCOFFIN
    {Fore.CYAN}0{Fore.RESET}|  EXIT
    {Fore.CYAN}1{Fore.RESET}|  Check for updates

    --------------- DISCORD
    {Fore.CYAN}2{Fore.RESET}|  Normal Spam
    {Fore.CYAN}3{Fore.RESET}|  Changelog
"""

if __name__ == "__main__":
    print(ascii_title)
    print(cmd_title)
    print(start_menu)