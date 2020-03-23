import win32clipboard as w
import win32con
import win32api
import win32gui
import time
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class weChatAccess():
    def __init__(self):
        self.help = 'help'

    def sendMsg(self, msg):
        hwnd = win32gui.FindWindow(None, '微信')
        if hwnd == 0:
            hwnd = win32gui.FindWindow(None, 'WeChat')
        if hwnd == 0:
            hwnd = win32gui.FindWindow(None, 'WeChat Beta')
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(1)
        setText(msg)
        ctrlV()
        altS()
        logger.info('Message sent:'+msg)
        # win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        # TODO: Close the wechat window

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


def setImage(data):  # write to Clipboard
    w.OpenClipboard()
    try:
        # Unicode tests
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_DIB, data)
    except:
        traceback.print_exc()
    finally:
        w.CloseClipboard()


def ctrlV():
    win32api.keybd_event(17, 0, 0, 0)  # ctrl
    win32api.keybd_event(86, 0, 0, 0)  # v
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # release the key
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


def altS():
    win32api.keybd_event(18, 0, 0, 0)  # Alt
    win32api.keybd_event(83, 0, 0, 0)  # s
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # release the key
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)

