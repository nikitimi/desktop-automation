import pyautogui

screenWidth, screenHeight = pyautogui.size()

print('Width: %s\tHeight: %s' % (screenWidth, screenHeight))

x, y = pyautogui.locateCenterOnScreen('src/images/file-explorer.jpg', confidence=0.9)
pyautogui.moveTo(x, y, duration=1, tween=pyautogui.easeInOutQuad)