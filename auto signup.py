import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from selenium import webdriver
import time
import sys
import os
from multiprocessing import Process
from selenium.common.exceptions import NoSuchElementException


def badname():
    tk.messagebox.showwarning(title='用户名错误！！', message=skyemail.get() + '用户名不存在')

def badpassword():
    bp = tk.messagebox.showwarning(title='密码错误！！', message=skyemail.get() + '密码错误')
    bp.replace(x=1700,y=100)
def locked():
    tk.messagebox.showwarning(title='账号被锁定！！', message=skyemail.get() + '被锁定')

def accept():
    tk.messagebox.showwarning(title='接受成功', message=skyemail.get() + '接受成功')

def limited():
    tk.messagebox.showwarning(title='限制！！', message=skyemail.get() + '被限制')

def loginn():

    #禁止加载图片
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)


    driver = webdriver.Chrome('D:\Python\Scripts\chromedriver.exe',chrome_options = chrome_options)
    driver.get('https://secure.skype.com/skypemanager/invite')
    # time.sleep()
    driver.find_element_by_name('loginfmt').send_keys(skyemail.get())
    time.sleep(0.5)
    driver.find_element_by_id('idSIButton9').click()
    time.sleep(0.5)
    try:
        driver.find_element_by_xpath("//div[@id='usernameError']")
        badname()
        driver.close()
    except:
        time.sleep(1)
        driver.find_element_by_name('passwd').send_keys(skypw.get() + '\n')

        # time.sleep(1)
        try:
            driver.find_element_by_xpath("//div[@id='passwordError']")
            badpassword()
            driver.close()
        except:
            pass
        try:
            driver.find_element_by_xpath('//*[@id="StartAction"]')
            locked()
            driver.close()
        except:
            pass
        try:
            time.sleep(0.3)
            driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
        except:
            pass
        try:
            driver.get('https://secure.skype.com/skypemanager/invite')
            driver.find_element_by_name('tos').click()
            time.sleep(0.2)
            driver.find_element_by_id('accept').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="notifications"]/div[1]')
            accept()
            driver.close()
        except:
                driver.find_element_by_xpath('//*[@id="pageBody"]/div[2]/div/div')
                limited()
                driver.close()


win = tk.Tk()

win.wm_attributes('-topmost',1)
win.title("接受管理员终极版")
# adding a label
aLabel = ttk.Label(win, text="输入账号:").grid(row=0)
skyemail = tk.StringVar()
emailEntered = ttk.Entry(win, width=30, textvariable=skyemail).grid(row=0, column=1)
blable = ttk.Label(win, text='输入密码：').grid(row=1)
skypw = tk.StringVar()
pwEntered = ttk.Entry(win, width=30, textvariable=skypw).grid(row=1, column=1)
confrimsky = ttk.Button(win, text='登录', command=loginn).grid(row=2, column=0)

win.mainloop()