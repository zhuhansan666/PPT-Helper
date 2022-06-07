# ------
debug = False
# ------
if debug:
    print("!警告!:  Debug模式 已开启")

NULL = None
import time
from subprocess import run
from sys import argv
from os.path import join,normpath

def reWorkPath() -> str:
    tempPath = argv[0]
    if '\\' in tempPath:
        tempPath = tempPath.replace(tempPath.split('\\')[-1],"")
    elif '/' in tempPath:
        tempPath = tempPath.replace(tempPath.split('/')[-1],"")
    return tempPath

workPath = reWorkPath()

with open(normpath(join(workPath,"startUp.reg")),"w+") as f:
    f.write("""Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run]

"awa"="{}" """.format(argv[0]))

with open(normpath(join(workPath,"startUp-MACHINE.reg")),"w+") as f:
    f.write("""Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run]

"awa"="{}" """.format(argv[0]))

run("regedit.exe /s {}".format(normpath(join(workPath,"startUp.reg"))),shell=True)
run("regedit.exe /s {}".format(normpath(join(workPath,"startUp-MACHINE.reg"))),shell=True)

if time.strftime("%A",time.localtime()) == "Friday" or debug:
    while True:
        timeStamp = float(time.mktime(time.strptime("{}|15:30:00".format(time.strftime("%Y-%m-%d",time.localtime())), "%Y-%m-%d|%H:%M:%S")))
        timeStamp2 = float(time.mktime(time.strptime("{}|16:00:00".format(time.strftime("%Y-%m-%d",time.localtime())), "%Y-%m-%d|%H:%M:%S")))
        if time.time() > timeStamp2:
            if not debug:
                try:
                    run("shutdown -s -f -t 0")
                except Exception:
                    try:
                        run("shutdown -s -f -t 0",shell=True)
                    except Exception:
                        pass
            else:
                print("Debug: 执行关机")
        elif time.time() > timeStamp:
            run(normpath(join(workPath,"kPowerpoint.exe")),shell=True)
        time.sleep(1)
else:
    timeStamp = float(time.mktime(time.strptime("{}|17:25:00".format(time.strftime("%Y-%m-%d",time.localtime())), "%Y-%m-%d|%H:%M:%S")))
    waitTime = timeStamp-time.time()
    if waitTime > 0:
        time.sleep(waitTime)
    del waitTime
    if not debug:
        try:
            run("shutdown -s -f -t 0")
        except Exception:
            try:
                run("shutdown -s -f -t 0",shell=True)
            except Exception:
                pass
    else:
        print("Debug: 执行关机")
