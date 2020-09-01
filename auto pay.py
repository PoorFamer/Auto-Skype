import json
from selenium import webdriver
import time

url = 'https://manager.skype.com/my/login'
driver = webdriver.Chrome()



def loginn():


    driver.get(url)
    # 删除第一次建立连接时的cookie
    driver.delete_all_cookies()
    # 读取本地的cookie文件
    with open('cook.json', 'r', encoding='utf-8') as f:
        list_cookies = json.loads(f.readline())
        #print(list_cookies)
        driver.get(url)
        driver.delete_all_cookies()

        for cookie in list_cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            driver.add_cookie(cookie)
        print('cookies加载完成')
        driver.get('https://manager.skype.com/my/members')
    # 读取完cookie刷新页面
    driver.refresh()

#默认邀请，账号从excel中获取，状态打印至excel，需要循环
#def invite():


#充值充能


def payment():
    print('向列表中添加账号（输入“sx”结束）')
    account = []
    while 1:
        lives = input('>>>')
        if (lives.strip() == "sx"):
            break
        else:
            account.append(lives)

    i = len(account)
    msg = '共有%d' % len(account) + '个账号'
    print(msg)
    for x in range(20):



        try:
            live = account[x]
            #driver.get('https://manager.skype.com/member/features?user=' + live)
            #driver.find_element_by_xpath("//span[@id='span-info-efd81569208a3fed0c749bd123dcd61f']//a").click()
            #driver.find_element_by_xpath('//*[@id="span-info-5ac7e2ed633e85c318b2f643f87d01e9"]/a').click()
            driver.get("https://manager.skype.com/buy/subscriptions?user="+live+"&referer=member.features")
            driver.get('https://manager.skype.com/buy/subscriptions?product-type=cn-mixed-400&offer-id=calling&sku-id=cn-mixed-400')
            driver.find_element_by_xpath('//*[@id="buy"]').click()#括号内为支付按钮的xpath
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[7]')#400分钟套餐lable
            print(live + '充值成功')

        except:

            print(live +'充值失败')


'''def quit():
        input('敲回车退出浏览器')
        driver.close()
'''

loginn()
# 账号列表


payment()
