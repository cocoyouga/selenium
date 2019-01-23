#coding=utf-8
from selenium import webdriver  
import time
class SeleniumDriver():
    def __init__(self,browser):
        self.driver = self.open_browser(browser)

    def open_browser(self,browser):
        try:
            if browser == 'chrome':
                driver = webdriver.Chrome()
            elif browser == 'firefox':
                driver = webdriver.Firefox()
            else:
                driver = webdriver.Ie()
            time.sleep(1) 
            return driver
        except:
            print('打开浏览器失败')
            return None

    def get_url(self,url):
        if self.driver != None:
            if 'http://' in url:
                self.driver.get(url)
            else:
                print('你的URL有问题')
        else:
            print('case失败')

    def handle_window(self,*args):
        value = len(args)
        if value == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.driver.minimize_window()
            elif args[0] == 'back':
                self.driver.back()
            elif args[0] == 'go':
                self.driver.forward()
            else:
                self.driver.refresh()
        elif value == 2:
            self.driver.set_window_size(args[0],args[1])
        else:
            print('你传递的参数有误')
        time.sleep(3)
        self.driver.quit()
selenium_driver = SeleniumDriver('chrome')
selenium_driver.handle_window('max')


    