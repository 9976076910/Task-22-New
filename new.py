from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class Testing:

    def __init__(self): # Constructor
        self.url = "https://www.instagram.com/guviofficial/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def getTextByXPATH(self, xpathLocator):
        return self.driver.find_element(By.XPATH, value=xpathLocator).text

    def clickElementByXPATH(self, xpathLocator):
        self.driver.find_element(By.XPATH, value=xpathLocator).click()

    def wait(self, secs=3):
        time.sleep(secs)

    def goBack(self):
        self.driver.back()

    def boot(self):
        self.driver.get(self.url)
        self.wait(4)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def followersAndFollowing(self):
        self.clickElementByXPATH('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[2]/div/div/div[1]/div/button/span')
        self.wait()
        print(self.getTextByXPATH("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span"))
        print(self.getTextByXPATH("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span"))



testing1 = Testing()
testing1.boot()
testing1.followersAndFollowing()
testing1.quit()

