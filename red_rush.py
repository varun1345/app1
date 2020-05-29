import pyautogui,time

time.sleep(6)


taker=True
taker1=False
counter=0
counter1=0



def function1(taker2,counter2):
    while taker2:
        if counter2 == 0:
            if pyautogui.pixelMatchesColor(959,931, (241, 94, 97)):
                if pyautogui.pixelMatchesColor(956, 509, (241, 94, 97)):
                    pyautogui.click(956, 561)
                    counter2 += 1

        if pyautogui.pixelMatchesColor(956, 700, (241, 94, 97)):
            function2(True,0)
            break
        if counter2 == 0:
            if pyautogui.pixelMatchesColor(959,931, (92, 162, 216)):
                if pyautogui.pixelMatchesColor(956, 509, (92, 162, 216)):
                    pyautogui.click(956, 561)
                    counter2 += 1

        if pyautogui.pixelMatchesColor(956, 700, (92, 162, 216)):

            function2(True,0)
            break
def function2(taker1,counter1):
    while taker1:
        if counter1 == 0:
            if pyautogui.pixelMatchesColor(956, 125, (241, 94, 97)):
                if pyautogui.pixelMatchesColor(956, 570, (241, 94, 97)):
                    pyautogui.click(956, 100)
                    counter1 += 1
        if pyautogui.pixelMatchesColor(960, 370, (241, 94, 97)):
            function1(True, 0)
            break

        if counter1 == 0:
            if pyautogui.pixelMatchesColor(960,125, (92, 162, 216)):
                if pyautogui.pixelMatchesColor(956, 570, (92, 162, 216)):
                    pyautogui.click(956, 100)
                    counter1 += 1

        if pyautogui.pixelMatchesColor(960, 370, (92, 162, 216)):

            function1(True,0)
            break
function1(taker,counter)
