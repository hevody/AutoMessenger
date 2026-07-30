import webbrowser
import time
import pyautogui
import os
import pyperclip

#os.chdir("C:\\Users\\tokyo\\Desktop")

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
time.sleep(5)

with open('senger.txt') as id:
    ids = id.readlines()

#print(ids)

def logIn():
    webbrowser.open("https://messenger.com")
    with open("senger.txt") as id:
        ids = id.readlines()
    time.sleep(5)
    userName = True
    for iden in ids:
        iden = iden.strip()
        if userName:
            pyautogui.click(x=294, y=1186)
        pyautogui.write(iden)
        pyautogui.hotkey("enter")
        time.sleep(1)
        userName = False

if "killswitch.txt" not in os.listdir():
    logIn()

time.sleep(10)

accounts = [["Sir Me", "https://www.messenger.com/", "AP"]]

link = accounts[0][1] 
webbrowser.open(link)

message = [f'Good afternoon po, {accounts[0][0]}!!!!! 🫡', f'Maaari niyo po bang isend ang PPT o activity sa subject na "{accounts[0][2]}" sa ating gc 🚀', ' ', 'Kung nasend niyo na naman po ay idisregard niyo na lang po itong message 😅', ' ', '🤖 Bot powered by Velocity']

time.sleep(10)

for messagePart in range(len(message)):
    pyperclip.copy(message[messagePart])
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('shift', 'enter')
pyautogui.hotkey('enter')











 