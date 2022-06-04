# -------------------
debug = False
# -------------------
if debug:
    print("!警告!:  Debug模式 已开启")

NULL = None
from os import remove
from os.path import exists
from win32gui import SetWindowPos,SetForegroundWindow
from win32con import HWND_TOPMOST,SWP_NOMOVE,SWP_NOSIZE
from win32com.client import Dispatch

def setActWin(hwnd):
    stop = False
    while not stop:
        try:
            shell = Dispatch("WScript.Shell")
            shell.SendKeys('%')
            stop = True
        except Exception:
            pass
    try:
        SetForegroundWindow(hwnd)
    except Exception:
        pass

def main():
    f = open("running.tmp","w+")
    import pywintypes
    from win32gui import MessageBox,FindWindow
    from win32con import MB_OK,MB_ICONERROR
    from threading import Thread
    from time import sleep
    from sys import argv

    title = "ERROR"
    info = "幻灯片启动失败 \n且课后服务上课属于非法行为/操作"

    if "-title" in argv[1:]:
        try:
            title = argv[argv.index("-title")+1]
        except IndexError:
            pass
    if "-info" in argv[1:]:
        try:
            info = argv[argv.index("-info")+1].replace('\\n','\n')
        except IndexError:
            pass

    t = Thread(target=lambda:MessageBox(NULL,info,title,MB_OK | MB_ICONERROR),daemon=True)
    t.start()

    hwnd = 0
    while hwnd == 0:
        hwnd = FindWindow(NULL,title)
    print(str(hwnd))
    f.write(str(hwnd))
    f.close()
    f2 = open("running.tmp","r+")
    SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 100, 100, SWP_NOMOVE | SWP_NOSIZE)
    setActWin(hwnd)
    if not debug:
        sleep(5)
    else:
        while True:
            try:
                pass
            except (KeyboardInterrupt or EOFError or Exception):
                break
    f2.close()
    try:
        remove("running.tmp")
    except Exception:
        pass

if exists("running.tmp"):
    try:
        remove("running.tmp")
        main()
    except Exception:
        try:
            with open("running.tmp","r+") as tmpFile:
                r = tmpFile.read()
        except Exception:
            r = NULL
        if r is not NULL:
            try:
                hwnd = int(r)
                SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 100, 100, SWP_NOMOVE | SWP_NOSIZE)
                setActWin(hwnd)
            except Exception:
                pass
else:
    main()

