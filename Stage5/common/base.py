import os
import platform


def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    if platform.system() == "Linux":
        os.system('clear')
