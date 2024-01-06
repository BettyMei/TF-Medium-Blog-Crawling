from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import utils

# 文章链接xpath拼接
pre = '//*[@id="root"]/div/div[3]/div[2]/div/div[4]/div/div[3]/div['
suf = ']/div/article/div/div/div/div/div[2]/div[1]/a[@href]'
path = "source_data/"

def get_href_xpath(pre, fn):
    xpathList = []
    for i in range(1, 11):
        xpath = pre+str(i)+fn
        xpathList.append(xpath)
    return xpathList


# 获取10篇文章(10 mest read)的url，在获取url手动点击页面上的【10 mest read】（selenium可以模拟人工点击，未实现）
def get_url_list(browser, hrefXPaths):
    url_list = []
    wait = WebDriverWait(browser, 10)
    for hrefXPath in hrefXPaths:
        ele = wait.until(EC.visibility_of_element_located((By.XPATH, hrefXPath)))
        url_list.append(ele.get_attribute('href'))
    return url_list


# 加载cookie
def get_cookie():
    driver = webdriver.Chrome(executable_path='D:\google\chromedriver-win64\chromedriver.exe')
    driver.get('https://medium.com/tag/software-engineering/archive')
    time.sleep(20)
    cookies = driver.get_cookies()
    # 将字典形式的 cookies 转换成 JSON 格式的字符串
    json_cookies = json.dumps(cookies)
    # 将 JSON 格式的 cookies 写入到本地文件
    utils.file_write("cookies.json", json_cookies)
    driver.quit()


if __name__ == '__main__':
    # get_cookie()
    # 加载页面并登录
    browser = webdriver.Chrome(executable_path='D:\google\chromedriver-win64\chromedriver.exe')
    browser.get('https://medium.com/tag/software-engineering/archive')
    json_cookies = utils.file_read("cookies.json")
    cookies = json.loads(json_cookies)
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.refresh()
    time.sleep(5)

    hrefXPaths = get_href_xpath(pre, suf)
    urls = get_url_list(browser, hrefXPaths)
    print(urls)
    num = 1
    for url in urls:
        browser.get(url)
        time.sleep(10)
        WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]/article/div/div/section/div/div[3]/div/div')))
        # 整个文章的xpath
        contents = browser.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div[2]/article/div/div/section/div/div[3]/div/div').text.strip()
        print(contents)
        utils.file_write(path+"article_"+str(num)+".txt", contents)
        num = num + 1

    browser.quit()

