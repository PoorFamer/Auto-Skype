from selenium import webdriver
import time
import json


url = ('https://manager.skype.com/my/login')
#获得cookies的登录流程

def login():

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_xpath("//button[@class='IzjkL _2Y_WL normal _2GPxk signUp']//span").click()
    time.sleep(0.5)
    print('请输入管理器账号：')
    username = input()
    driver.find_element_by_xpath("//input[@id='i0116']").send_keys(username)
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(2)
    print('请输入管理器密码：')
    password = input()
    driver.find_element_by_xpath("//input[@id='i0118']").send_keys(password + '\n')
    time.sleep(2)
    driver.refresh()
    time.sleep(1)
    #获取cookies
    cookie = driver.get_cookies()
    print(cookie)
    jsonCookies = json.dumps(cookie)
    with open('cook.json', 'w') as f:
        f.write(jsonCookies)

    time.sleep(5)
    driver.quit()

login()




