from Crypto.Cipher import AES
import base64
import time
import tkinter
import win32clipboard as w
import win32con
import win32api
import win32gui
import logging
import gui
import weChatAccess
import encryption


if __name__ == '__main__':
    newGui = gui.SafeChatGui
    newGui.initialize()
