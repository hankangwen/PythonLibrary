# 03、截图
# 现在，你可以使用下面这个很棒的脚本以编程方式截取屏幕截图。 使用此脚本，你可以直接截屏或截取特定区域的屏幕截图。
# Grab Screenshot
# pip install pyautogui
# pip install Pillow

from pyautogui import screenshot
import time
from PIL import ImageGrab


# Grab Screenshot of Screen
def grab_screenshot():
    shot = screenshot()
    # shot.save('my_screenshot.png')
    shot.save('e:\my_screenshot.png')


# Grab Screenshot of Specific Area
def grab_screenshot_area():
    area = (0, 0, 500, 500)
    shot = ImageGrab.grab(area)
    # shot.save('my_screenshot_area.png')
    shot.save('e:\my_screenshot_area.png')


# Grab Screenshot with Delay
def grab_screenshot_delay():
    time.sleep(5)
    shot = screenshot()
    # shot.save('e:\my_screenshot_delay.png')
    shot.save('my_screenshot_delay.png')
