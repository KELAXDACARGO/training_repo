import pyautogui
import time
import sys

try:
    img_detail_btn = 'D:/tardis/AUTOMATION/img/detail_btn_norm.png'   # clickable target img on the page. size = w:107px, h:62px  
    img_pull_down_menu = 'D:/tardis/AUTOMATION/img/pull_down_menu.png'# w:415px, h:30px
 
    #print(pyautogui.position())
    
    pyautogui.PAUSE = .5
    batches = int(pyautogui.prompt('how many awbs?'))
    #time.sleep(6)
    
    detail_btn_norm = None
    pull_down_menu = None
    confirm_button = None
    yes_button = None
    error_msg = None
    error_return_button = None
    y_delta = 27

    for i in range(batches):

        print(f"{i=}")

        if i <= 1:

            for y in range(390, 600, 5):
                for x in range(1780, 1820, 5):
                    detail_btn_norm = pyautogui.locateOnScreen(img_detail_btn, region=(x, y, 110, 60), confidence = .30)
                    if detail_btn_norm != None:
                        print (detail_btn_norm)
                        # detail_btn_norm = (detail_btn_norm.left + int(.55 * detail_btn_norm.width), detail_btn_norm.top + int(.55 * detail_btn_norm.height), detail_btn_norm.width, detail_btn_norm.height)
                        break
                if detail_btn_norm != None:
                    break

            # print (detail_btn_norm)

            pyautogui.moveTo(detail_btn_norm)
            time.sleep(1)
            pyautogui.click(detail_btn_norm)

            time.sleep(3.0)

            pyautogui.typewrite(["pgdn"])
            pyautogui.typewrite(["pgdn"])
            pyautogui.click()

            time.sleep(.5)

            for y in range(790, 820, 10):
                for x in range(640, 980, 10):
                    pull_down_menu = pyautogui.locateOnScreen(img_pull_down_menu, region=(x, y, 430, 30), confidence = .30)
                    if pull_down_menu != None:
                        break
                if pull_down_menu != None:
                    break

    #        print (pull_down_menu)

            pyautogui.moveTo(pull_down_menu)
            time.sleep(.2)
            pyautogui.click(pull_down_menu)
            pyautogui.click(pull_down_menu)
            #pyautogui.typewrite(["home"])
            time.sleep(.2)
            pyautogui.typewrite(["down"])
    #        pyautogui.typewrite(["enter"])       
            time.sleep(.2)
            pyautogui.typewrite(["tab"])
            pyautogui.typewrite(["tab"])
            pyautogui.typewrite(["space"])

    #        confirm_button = None
    #        while confirm_button == None:
    #            confirm_button = pyautogui.locateOnScreen('D:/tardis/AUTOMATION/img/confirm_button.png', region=(1780, 530, 120, 180), confidence = .30)
    #        confirm_button = (confirm_button.left + int(.49 * confirm_button.width), confirm_button.top + int(.50 * confirm_button.height))
    #        print (confirm_button)

    #        pyautogui.moveTo(confirm_button)
    #        pyautogui.click(confirm_button)
    #        confirm_button = None

            time.sleep(3)

            while yes_button == None:
                yes_button = pyautogui.locateOnScreen('D:/tardis/AUTOMATION/img/yes_button.png', region=(1860, 250, 60, 45), confidence = .40)
            #print (yes_button)

            pyautogui.moveTo(yes_button)
            pyautogui.click(yes_button)
            time.sleep(4.5)

            #pyautogui.typewrite(["delete"])
            #pyautogui.typewrite("corona virus")
            #pyautogui.typewrite(["enter"])

        else:
            pyautogui.moveTo(detail_btn_norm)
            time.sleep(1)
            pyautogui.click(detail_btn_norm)

            time.sleep(1.5)

            # pyautogui.typewrite(["pgdn"])
            # pyautogui.typewrite(["pgdn"])
            # pyautogui.click()

            # time.sleep(.5)

            pyautogui.moveTo(pull_down_menu)
            time.sleep(.2)
            pyautogui.click(pull_down_menu)
            pyautogui.click(pull_down_menu)
            #pyautogui.typewrite(["home"])
            time.sleep(.2)
            pyautogui.typewrite(["down"])
    #        pyautogui.typewrite(["enter"])       
            time.sleep(.2)
            pyautogui.typewrite(["tab"])
            pyautogui.typewrite(["tab"])
            pyautogui.typewrite(["space"])

            time.sleep(2.0)

            while yes_button == None:
                yes_button = pyautogui.locateOnScreen('D:/tardis/AUTOMATION/img/yes_button.png', region=(1860, 250, 60, 45), confidence = .40)
            #print (yes_button)

            pyautogui.moveTo(yes_button)
            pyautogui.click(yes_button)
            time.sleep(3.0)

except KeyboardInterrupt:
    sys.exit()