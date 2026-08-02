import pyautogui
import time
import webbrowser

# if perhaps you are running on brave web browser like I do, might as well uncomment the following code
# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
# webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))

# --- CONFIG --- #
LIGHT_MODE = True

if LIGHT_MODE == True:
  find_color = (240, 242, 245)
else: 
  find_color = (58, 59, 60)

screen = pyautogui.size()

constant_y = 1296 # this can change depending on the windows computer, so if you know what you're doing, you can change this depending on your needs or for compatability
width = screen.width

# --- #

def capturing_w_px():
    for width_px in range(width):
      color = pyautogui.pixel(width_px, constant_y)
      if color == find_color:
        captured_width_px = width_px + 20 # 20 is an allowance
        Found = True
        return captured_width_px, Found

def load_messenger():
  webbrowser.open("https://www.facebook.com/messages/")   # the account goes here
  time.sleep(5)

def find_the_pixel_for_typewrite():      
  captured_width_px = 0
  Found = False
  while not Found:
    try:
      captured_w_px, Found = capturing_w_px()
    except TypeError:
      continue

  pyautogui.doubleClick(captured_w_px, constant_y)  

def send_message():
  for _ in range(20):
    pyautogui.typewrite("hello, world!")
    time.sleep(0.5)
    pyautogui.press('enter')

def load_csv():
  pass  # feature coming soon

if __name__ == '__main__':
  load_messenger()
  find_the_pixel_for_typewrite()
  send_message()
