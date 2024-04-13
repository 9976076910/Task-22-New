from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


class LoginAutomation:
    def __init__(self, url="https://www.instagram.com/guviofficial/"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(3)

    def quit(self):
        self.driver.quit()

    # def findElementByfullXPath(self, fullXpath):
    # return self.driver.find_element(by=By.XPATH, value=fullXpath)

    def goToFollowers(self):
        self.boot()
        sleep(3)
        self.driver.find_element(by=By.XPATH,
                                 value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[2]/div/div/div[1]/div/button/span').click()
        sleep(2)

        practiceElement = self.driver.find_element(By.XPATH,
                                                   '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span').text
        practiceElement1 = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span').text
        print(practiceElement)
        print(practiceElement1)
        self.driver.quit()


obj = LoginAutomation()
obj.goToFollowers()
