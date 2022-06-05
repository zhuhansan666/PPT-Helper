#include <iostream>
#include <fstream>
#include <windows.h>
#include <setjmp.h>

using namespace std;

static jmp_buf checked;

BOOL CALLBACK append(HWND hwnd,LPARAM lParam) {
    char WinTitle[99999];
    GetWindowText(hwnd,WinTitle,sizeof(WinTitle));
    checked:
    if (strstr(WinTitle,"PowerPoint") != NULL) 
    {   
        SendMessage(hwnd,WM_CLOSE,NULL,NULL);
        system("start messageBox.exe");
        longjmp(checked,1); // 解决重复获取到PPT句柄的问题
    }
    return true;
}

int subMain() {
    while (1) {
        EnumChildWindows(NULL,append,(LPARAM)NULL);
        if (setjmp(checked) == 1) // 延时以解决问题
        {
            Sleep(300);
        } else {
            Sleep(10); // 正常延时
        }
    }
    return 0;
}

int main(int argc, char *argv[]) {
    ShowWindow(FindWindow("ConsoleWindowClass",argv[0]),0); //使用WInAPI隐藏窗口-有效但会闪过一瞬间,且必须放在 main(int argc,char *argv[]) 内
    ofstream f;
    ifstream file("run.tmp");
    if (file.good()) {
        file.close(); // remove 前记得关掉!!! 不然自己会占用自己!!!
        if (!remove("run.tmp"))
        {
            f.open("run.tmp");
            subMain();
        }
    } else {
        file.close();
        f.open("run.tmp");
        subMain();
    }
    return 0;
}

