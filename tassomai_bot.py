from selenium import webdriver
from config import email, password, browser
import time
browser = browser.lower()
if browser != "chrome":
    if browser != "firefox":
        print("Incorrect browser selected, please choose either Chrome or Firefox")
        exit()
else:
    pass

class TassomaiBot():
    def __init__(self):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get("https://app.tassomai.com/login")
        email_bx = self.driver.find_element_by_xpath('/html/body/tasso-app/tasso-entry/div/div/login/div/tabset/div/tab/div[3]/login-form/form/div[1]/input')
        email_bx.send_keys(email)
        pass_bx = self.driver.find_element_by_xpath('/html/body/tasso-app/tasso-entry/div/div/login/div/tabset/div/tab/div[3]/login-form/form/div[2]/input')
        pass_bx.send_keys(password)
        login_btn = self.driver.find_element_by_xpath('/html/body/tasso-app/tasso-entry/div/div/login/div/tabset/div/tab/div[3]/login-form/form/div[3]/button')
        login_btn.click()
    
    def answer1(self):
        a1_btn = self.driver.find_element_by_xpath('/html/body/tasso-app/tasso-entry/div/div/learner-dashboard/quiz-modal/div[2]/quiz/div/swiper/div/div[1]/div[1]/swiper/div/div[1]/div[3]/swiper/div/div[1]/div[1]/question/div[2]/div[1]/answer/button/span[3]')
        a1_btn.click()
    def answer2(self):
        a2_btn = self.driver.find_element_by_xpath('/html/body/tasso-app/tasso-entry/div/div/learner-dashboard/quiz-modal/div[2]/quiz/div/swiper/div/div[1]/div[1]/swiper/div/div[1]/div[3]/swiper/div/div[1]/div[2]/question/div[2]/div[1]/answer/button/span[3]')
        a2_btn.click()
    def answer3(self):
        a3_btn = self.driver.find_element_by_xpath('/html/body/tasso-app/tasso-entry/div/div/learner-dashboard/quiz-modal/div[2]/quiz/div/swiper/div/div[1]/div[1]/swiper/div/div[1]/div[3]/swiper/div/div[1]/div[3]/question/div[2]/div[1]/answer/button/span[3]')
        a3_btn.click()
    def answer4(self):
        a4_btn = self.driver.find_element_by_xpath('/html/body/tasso-app/tasso-entry/div/div/learner-dashboard/quiz-modal/div[2]/quiz/div/swiper/div/div[1]/div[1]/swiper/div/div[1]/div[3]/swiper/div/div[1]/div[4]/question/div[2]/div[1]/answer/button/span[3]')
        a4_btn.click()
    def continuebtn(self):
        cont_btn = self.driver.find_element_by_xpath('/html/body/tasso-app/tasso-entry/div/div/learner-dashboard/quiz-modal/div[2]/quiz/div/swiper/div/div[1]/div[1]/swiper/div/div[1]/div[3]/swiper/div/div[1]/div[5]/quiz-score/button')
        cont_btn.click()
    def continue2btn(self):
        cont2_btn = self.driver.find_element_by_xpath('/html/body/tasso-app/tasso-entry/div/div/learner-dashboard/quiz-modal/div[2]/button')
        cont2_btn.click()
    def startbtn(self):
        start_btn = self.driver.find_element_by_xpath('/html/body/tasso-app/tasso-entry/div/div/learner-dashboard/div/tass-goal-page/div/div[2]/tass-quiz-suggestions-container/tass-quiz-suggestions/div/div[2]/tass-start-quiz-container[1]/tass-start-quiz/div/div[2]/div[2]/button')
        start_btn.click()

try:

    bot = TassomaiBot()
    bot.login()
except:
    print("Geckodriver not found in PATH, please instructions at https://github.com/sharp312/tassomaibot/wiki/Windows-10-setup-instructions")
    exit()
#start = input("Press enter when logged in")

time.sleep(2)
while True:
    bot.startbtn()
    time.sleep(2)
    bot.answer1()
    time.sleep(3)
    bot.answer2()
    time.sleep(3)
    bot.answer3()
    time.sleep(3)
    bot.answer4()
    time.sleep(3)
    bot.continuebtn()
    time.sleep(2)
    bot.continue2btn()
    time.sleep(2)
