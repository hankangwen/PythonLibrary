# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyautogui
import pyperclip
import time, random

def start():
    time.sleep(3)  # 软件启动后等3秒才执行，这个时间内你立马把鼠标移到要打字的地方（我就放到VS上）
    for line in open(r"D:\test.txt", encoding='utf-8'):  # 这是要读取的文本（我放了代码）的地址
        for i in line:
            pyperclip.copy(i)  # 读取数据
            pyautogui.typewrite('{}'.format(i))  # 模拟写数据
    # 模拟按“Ctrl+S”保存
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('s')
    pyautogui.keyUp('s')
    pyautogui.keyUp('ctrl')
    time.sleep(2)  # 保存后给它缓一下

