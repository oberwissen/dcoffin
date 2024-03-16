import os
import sys
from colorama import Fore, Style

from LANG import selected
from projekt import general

input_text = f"{Fore.RED}{Style.BRIGHT}{general.name}{Fore.BLUE}@python{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} {Style.RESET_ALL}$ "

thread_list = []

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def set_terminal_title():
    if selected.selected_lang == "TR":
        from LANG import turkish as string
    else:
        from LANG import english as string
    if os.name == "nt":
        os.system(f"title {string.cmd_title}")
    else:
        sys.stdout.write(f"\x1b]2;{string.cmd_title}\x07")

def terminate(reason=None):
    sys.exit()


def line():
    width = os.get_terminal_size().columns
    return '-' * width

def setup():
    print("EN Select a language - TR Bir dil seçin")
    print("""
    
    0| EN
    1| TR
    
    """)
    choose = str(input(" $ "))
    with (open("OBER/lang.txt", "w") as lang_file):
        if choose == "1":
            lang_file.write("TR")
        else:
            lang_file.write("EN")
    with open("OBER/is_first_time.txt", "w") as first_time_file:
        first_time_file.write("0")
    clear_terminal()

