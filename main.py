# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import extracthtml
import qrcodeScanner
import screenshot
import copyCode
import createQRCode
import sendWechat
from YamlConfig import TestYaml


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Kerven')
    TestYaml.start()
    # qrcodeScanner.start()
    # sendWechat.start()
    # createQRCode.createWithIcon()
    # copyCode.start()
    # screenshot.grab_screenshot()
    # screenshot.grab_screenshot_area()
    # screenshot.grab_screenshot_delay()
    # extract_html.start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
