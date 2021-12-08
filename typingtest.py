
from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
import time
import keyboard

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.get("https://10fastfingers.com/typing-test/english")

time.sleep(6)
word_list = []

cookies_button = pyautogui.locateCenterOnScreen("AllowCookies.PNG")
pyautogui.moveTo(cookies_button[0],cookies_button[1],duration=3)
pyautogui.click(cookies_button[0],cookies_button[1],button="left")

time.sleep(2)
def reset_words_list(words_list):
    text_elements = driver.find_elements(By.XPATH,"//div[@id='row1']/span")
    words_list = [i.get_attribute("textContent") for i in text_elements]
    return words_list

word_list = reset_words_list(word_list)
#start typing test
start_typing_test_button = pyautogui.locateCenterOnScreen("Capture.PNG")
pyautogui.moveTo(start_typing_test_button[0],start_typing_test_button[1],duration=3)
pyautogui.click(start_typing_test_button[0],start_typing_test_button[1],button="left")
timeout = time.time() + 60

for word in word_list:
    if time.time() > timeout:
        break
    else:
        pyautogui.typewrite(word + " ")
        time.sleep(0.02)
driver.quit()
