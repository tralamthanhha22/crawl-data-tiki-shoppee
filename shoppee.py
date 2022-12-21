#type="application/ld+json"
import time
import io
import csv
from time import sleep
from matplotlib import image
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
n=1
if n==1:
    go="https://shopee.vn/Th%E1%BB%9Di-Trang-N%E1%BB%AF-cat.11035639?page="
elif n=="nam":
   go="https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567?page="
elif n=="kid":
    go="https://shopee.vn/search?keyword=qu%E1%BA%A7n%20%C3%A1o%20tr%E1%BA%BB%20em&page="
for l in range(5):
    print("===================================="+str(l)+"=================================")
    driver.get(go+str(l))
    html = driver.find_element_by_tag_name('body')
    # Keys.PAGE_DOWN cho cuộn xuống 100 lần
    for i in range(5):
        html.send_keys(Keys.PAGE_DOWN)  
    links=driver.find_elements_by_xpath("//a[@href]")
    a=[]
    level_counter=0
    for row in links:
        if len(row.get_attribute('href'))>70:
            a.append(row.get_attribute('href'))
    contents1=[]
    likes1=[]
    details1=[]
    stars1=[]
    if n==1:
        f=open("shopee_woman_all.csv","w",encoding="utf8")
    elif n=="nam":
        f=open("shopee_men_all.csv","a",encoding="utf8")
    elif n=="kid":
        f=open("shopee_kid_all.csv","w",encoding="utf8")
    for nguyenthanhan in a:
        if "buyer" or "help" not in nguyenthanhan:
            driver.get(str(nguyenthanhan))
        body=driver.find_element_by_tag_name('body')
        for i in range(5):
            body.send_keys(Keys.PAGE_DOWN)  
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        type=driver.find_elements_by_xpath("//script[@type='application/ld+json']")
        for i in type:
            if "Product" in i.get_attribute('innerHTML'):
                a=i.get_attribute('innerHTML').split(",")
                import re
                for j in range (len(a)):
                    print(a[j])
                    print("============================")
                    print(re.findall(r'.*((".+"):(".*"|[0-9])).*',a[j]))
                    li = re.findall(r'.*((".+"):(".*"?|[0-9])).*',a[j])
                    f.write(li[0][0]+"\n")
    f.close()
print("+++++++++++++++++++++++++++++++++++++++      DONE ALL              ++++++++++++++++++++++++++++++++++++++++++++++++++")
driver.close()