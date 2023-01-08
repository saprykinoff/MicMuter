import time

import keyboard
from win10toast import ToastNotifier
import winsound
import pystray
import PIL.Image
# import pym
import win32api
import win32gui

WM_APPCOMMAND = 0x319
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000

toast = ToastNotifier()
NAME = "MicMuter"

import os
import sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()
    return os.path.join(base_path, relative_path)

def notify(state:bool):
    print(state)
    if (not state):
        freq = 440
        duration = 400
    else:
        freq = 800
        duration = 600
    winsound.Beep(freq, duration)
state = True
if state:
    img = PIL.Image.open(resource_path('on.ico'))
else:
    img = PIL.Image.open(resource_path('off.ico'))



def my_exit(icon, item):
    icon.stop()




icon = pystray.Icon('MicMute', img, menu=pystray.Menu(
    pystray.MenuItem("Выход", my_exit),

))


def change_state():
    global state
    state = not state
    if state:
        img = PIL.Image.open(resource_path('on.ico'))
    else:
        img = PIL.Image.open(resource_path('off.ico'))
    icon.icon = img



def change():
    print("pressed")
    global state
    state = not state
    hwnd_active = win32gui.GetForegroundWindow()
    win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)

    if state:
        img = PIL.Image.open(resource_path('on.ico'))
    else:
        img = PIL.Image.open(resource_path('off.ico'))
    icon.icon = img
    notify(state)





keyboard.add_hotkey("ctrl+\\", change)
keyboard.add_hotkey("ctrl+alt+[", change_state)
icon.run()
# keyboard.add_hotkey()