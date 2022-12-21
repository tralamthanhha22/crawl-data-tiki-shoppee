b#id="__NEXT_DATA__"(tiki)
import time
import io
import csv
from time import sleep
#from matplotlib import image
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
n=2
if n==1:
    tr="https://tiki.vn/thoi-trang-nu/c931?sort=top_seller&page="
elif n==2:
    tr="https://tiki.vn/thoi-trang-nam/c915?sort=top_seller&page="
elif n==3:
    tr="https://tiki.vn/thoi-trang-cho-me-va-be/c11603&page="
elif n==4:
    tr="https://tiki.vn/thoi-trang-be-gai/c5189?sort=top_seller&page="
elif n==5:
    tr="https://tiki.vn/thoi-trang-be-trai/c5190?sort=top_seller&page="
elif n==6:
    tr="https://tiki.vn/quan-ao-so-sinh/c5252?sort=top_seller&page="
elif n==7:
    tr="https://tiki.vn/thoi-trang-me-bau/c5191?sort=top_seller&page="
elif n==8:
    tr="https://tiki.vn/bo-ao-lien-quan/c5253?sort=top_seller&page="
option = Options()
#sleep(3)
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})
for i in range(1,99):
    print("===================================="+str(i)+"=================================")
    driver.get(tr+str(i))
    html = driver.find_element_by_tag_name('body')
    # time.sleep(3)
    # Keys.PAGE_DOWN cho cuộn xuống 100 lần
    for i in range(1):
    # to make scroll to page bottom
        html.send_keys(Keys.PAGE_DOWN)  
        #time.sleep(2)
    links=driver.find_elements_by_xpath("//a[@href]")
    a=[]
    for row in links:
        if len(row.get_attribute('href'))>70:
            a.append(row.get_attribute('href'))
    contents1=[]
    stars1=[]
    details1=[]
    if n==4:
        f="tiki_girl__kid_pag1.txt"
    elif n==1:
        f="tiki_women_all.txt"
    elif n==2:
        f=open("tiki_men_all.txt","w",encoding="utf8")
    elif n==5:
        f="tiki_momBaby_all.txt"
    elif n==5:
        f="tiki_boy_kid_p1.txt"
    elif n==7:
        f="tiki_pregnant_p1.txt"
    elif n==6:
        f="tiki_baby_p1.txt"
    elif n==8:
        f="tiki_baby_bo-ao-lien-quan_p1.txt"
    f.write("thinh master-id thinh tlth thinh sku thinh")
    for nguyenthanhan in a:
        driver.get(nguyenthanhan)
        print(nguyenthanhan)
        body=driver.find_element_by_tag_name('body')
        for an in range(5):
            body.send_keys(Keys.PAGE_DOWN)  
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        re=driver.find_elements_by_xpath("//script[@type='application/json']")
        #re=driver.find_elements_by_xpath("//script[@type='application/ld+json']")
        for i in range (len(re)):
                dic=re[i].get_attribute('innerHTML')
            #if "Product" in dic:
                dic1=dic.split(",")
                dic2=dic.split(":[{")
                dic3=dic.split(":")
                for e in range(len(dic3)):
                    if "categories" in dic3[e]:
                        print(dic3[e])
                # for d in range(len(dic2)):
                    # if "configurable_options" in dic2[d]: #ok
                    #     print(dic2[d+1]+" "+dic2[d+2])
                    # if "configurable_products" in dic2[d]: #ok
                    #     print(dic2[d+1]+" "+dic2[d+2])
                # for j in range(len(dic1)):
                #     print(dic1[j])
                    # if "master_id" in dic1[j]:#ok
                    #     print(dic1[j])
                    #     f.write("thinh "+dic1[j]+"thinh tlth")
                    # elif "sku" in dic1[j]:# sku đầu tiên #oke nhen
                    #     print(dic1[j])
                    #     f.write("thinh "+dic1[j]+"thinh tlth")
                    # elif "url_key"in dic1[j]:#oke nhen
                    #      print(dic1[j])
                    #      f.write("thinh"+dic1[j]+"thinh tlth")
                    # elif "url_path"in dic1[j]:
                    #      print(dic1[j+1])
                    # elif "keyword" in dic1[j]:#oke nhen, co van de
                    #     f.write("thinh")
                    #     print(dic1[j])
                    #     f.write(dic1[j]+"thinh tlth")
                    # # if "type"in dic1[j]:
                    # #      print(dic1[j])
                    # # if "short_description"in dic1[j]:
                    # #      print(dic1[j])
                    # # if "price"in dic1[j]:
                    # #      print(dic1[j])
                    # elif "discount" in (dic1[j]):#oke nhen
                    #     print(dic1[j])
                    #     f.write("thinh"+dic1[j]+"thinh tlth")
                    # elif "badges"in dic1[j]:#oke nhen
                    #      print(dic1[j])
                    #      f.write("thinh"+dic1[j]+"thinh tlth")
                    # elif "review_count"in dic1[j]:#oke nhen
                    #      print(dic1[j])
                    #      f.write("thinh"+dic1[j]+"thinh tlth")
                    # if "order_count"in dic1[j]:
                    #      print(dic1[j])
                    # if "favorite_count"in dic1[j]:
                    #      print(dic1[j])
                    # elif "thumbnail_url"in dic1[j]: #oke nhen
                    #       print(dic1[j])
                    #       f.write("thinh"+dic1[j]+"thinh tlth")
                    # if "has_ebook"in dic1[j]: 
                    #       print(dic1[j])      
                    # if "inventory_status"in dic1[j]: 
                    #       print(dic1[j])    
                    # if "is_visible"in dic1[j]: 
                    #       print(dic1[j])
                    # if "productset_group_name"in dic1[j]: 
                    #       print(dic1[j])
                    # elif "is_fresh"in dic1[j]: #oke nhen
                    #       print(dic1[j])
                    #       f.write("thinh"+dic1[j]+"thinh tlth")
                    # elif "is_flower"in dic1[j]: #oke nhen
                    #       print(dic1[j])
                    #       f.write("thinh"+dic1[j]+"thinh tlth")
                    # elif "is_gift_card"in dic1[j]: #oke nhen
                    #       print(dic1[j])
                    #       f.write("thinh"+dic1[j]+"thinh tlth")
                          #itemQty
                    # if "inventory"in dic1[j]: 
                    #       print(dic1[j])
                    # if "url_attendant_input_form"in dic1[j]: 
                    #       print(dic1[j])    
                    # if "salable_type"in dic1[j]: 
                    #       print(dic1[j])
                    # if "data_version"in dic1[j]: #ok
                    #       print(dic1[j])    
                    # if "categories"in dic1[j]: 
                    #       print(dic1[j])
                    # if "liked"in dic1[j]: 
                    #       print(dic1[j])    
                    # if "rating_summary"in dic1[j]: 
                    #     print(dic1[j])
                    # if "description"in dic1[j]: 
                    #       print(dic1[j])    
                    # if "return_policy"in dic1[j]: 
                    #       print(dic1[j])
                    # if "brand"in dic1[j]: 
                    #       print(dic1[j])    
                    # if "seller_specifications"in dic1[j]: 
                    #       print(dic1[j])
                    # if "current_seller"in dic1[j]: 
                    #       print(dic1[j])    
                    # if "other_sellers"in dic1[j]: 
                    #       print(dic1[j])
                    # if "configurable"in dic1[j]: 
                    #       print(dic1[j])    
                    # if "configurable_products"in dic1[j]: 
                    #       print(dic1[j])
                    # if "specifications"in dic1[j]: 
                    #       print(dic1[j])    
                    # if "services_and_promotions"in dic1[j]: 
                    #       print(dic1[j])
                    # if "promotions"in dic1[j]: 
                    #       print(dic1[j])    
                    # if "stock_item"in dic1[j]: 
                    #       print(dic1[j])
                    # if "installment_info"in dic1[j]: 
                    #       print(dic1[j])    
                    # if "cloth_type"in dic1[j]: 
                    #       print(dic1[j])
                    # if "last_update"in dic1[j]: 
                    #       print(dic1[j])
                    # elif "is_seller_in_chat_whitelist"in dic1[j]: #oke nhen
                    #       print(dic1[j])
                    #       f.write("thinh"+dic1[j]+"thinh tlth")
                print("\n\n==============================")
print("+++++++++++++++++++++++++++++++++++++++      DONE ALL              ++++++++++++++++++++++++++++++++++++++++++++++++++")
f.close()
driver.close()
#link seller: //*[@id="__next"]/div[1]/main/div[3]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/a