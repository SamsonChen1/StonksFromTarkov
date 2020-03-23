import win32api
import win32con
import numpy as np
import time

_VK_CODE = {
    'backspace': 0x08,
    'tab': 0x09,
    'clear': 0x0C,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'caps_lock': 0x14,
    'esc': 0x1B,
    'spacebar': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'select': 0x29,
    'print': 0x2A,
    'execute': 0x2B,
    'print_screen': 0x2C,
    'ins': 0x2D,
    'del': 0x2E,
    'help': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
}

def long_sleep():
    time.sleep(10)

def short_sleep():
    time.sleep(np.random.uniform(.001, .003))


def get_position():
    return win32api.GetCursorPos()


def move_relative(x, y):
    # Adjust for windows API:
    x = int(round(x * 65535 / win32api.GetSystemMetrics(0)))
    y = int(round(y * 65535 / win32api.GetSystemMetrics(1)))

    # Move the mouse:
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)


def click():
    x, y = get_position()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    short_sleep()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def type(s):
    for c in s:
        if c not in _VK_CODE:
            raise Exception(f"Cannot type character {c}")
        else:
            win32api.keybd_event(_VK_CODE[c], 0, 0, 0)
            short_sleep()
            win32api.keybd_event(_VK_CODE[c], 0, win32con.KEYEVENTF_KEYUP, 0)


def hit_enter():
    win32api.keybd_event(_VK_CODE['spacebar'], 0, 0, 0)
    short_sleep()
    win32api.keybd_event(_VK_CODE['spacebar'], 0, win32con.KEYEVENTF_KEYUP, 0)
