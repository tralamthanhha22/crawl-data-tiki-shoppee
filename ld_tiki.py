#id="__NEXT_DATA__"(tiki)
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
        f=open("brand_tiki_men.csv","w",encoding="utf8")
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
    f.write("Brand,'',")
    for nguyenthanhan in a:
        driver.get(nguyenthanhan)
        print(nguyenthanhan)
        body=driver.find_element_by_tag_name('body')
        for an in range(1):
            body.send_keys(Keys.PAGE_DOWN)  
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        re=driver.find_elements_by_xpath("//script[@type='application/json']")
        re1=driver.find_elements_by_xpath("//script[@type='application/ld+json']")
        for i in re1:
            if "Product" in i.get_attribute('innerHTML'):
                dic1=i.get_attribute('innerHTML').split(":[")
                for j in range(len(dic1)):
                    if "Brand" in dic1[j]: #oke nhen
                        print(dic1[j+1].replace("manufacturer","").replace("}","").replace(",",""))
                        f.writelines(dic1[j+1].replace("manufacturer","").replace("}","").replace(",","")+",")
                    #print("😁😁😁😁😁😁😁😁😁😁😁😁")
                    # elif "sku" in dic1[j]: #oke nhen
                    #     print(dic1[j+1].replace("mpn","").replace(",",""))
                    # if "reviewCount"in dic1[j]: #ok, review count
                    #     print(dic1[j+1].replace("bestRating","").replace(",",""))
                    # if "type"in dic1[j]:
                    #     print(dic1[j+1])
                    # if "short_description"in dic1[j]:
                    #     print(dic1[j+1])
                    # if "order_count"in dic1[j]:
                    #     print(dic1[j])
                # print("😁😁😁😁😁😁😁😁😁😁😁😁")
                #     if "favorite_count"in dic1[j]:
                #         print(dic1[j])
                # print("😁😁😁😁😁😁😁😁😁😁😁😁")
                    # if "has_ebook"in dic1[j]: 
                    #     print(dic1[j])
                    #     print("😁😁😁😁😁😁😁😁😁😁😁😁")      
                    # if "inventory_status"in dic1[j]: 
                    #     print(dic1[j])
                    #     print("😁😁😁😁😁😁😁😁😁😁😁😁")    
                    # if "is_visible"in dic1[j]: 
                    #       print(dic1[j])
                        # if "productset_group_name"in dic1[j]: 
                        #       print(dic1[j])
                        # if "inventory"in dic1[j]: 
                        #       print(dic1[j])
                        # if "url_attendant_input_form"in dic1[j]: 
                        #       print(dic1[j])    
                        # if "salable_type"in dic1[j]: 
                        #       print(dic1[j])
                        # if "data_version"in dic1[j]: 
                        #       print(dic1[j])    
                        # if "categories"in dic1[j]: 
                        #       print(dic1[j])
                        # if "liked"in dic1[j]: 
                        #       print(dic1[j])    
                    # if "bestRating"in dic1[j]: #ok
                    #     print(dic1[j])
                    # elif "worstRating"in dic1[j]: #ok
                    #     print(dic1[j])
                    # elif "ratingValue"in dic1[j]: #ok
                    #     print(dic1[j])
                    # elif "description"in dic1[j]: #ok
                    #     print(dic1[j])    
                        # if "return_policy"in dic1[j]: 
                        #       print(dic1[j])
                        # if "seller_specifications"in dic1[j]: 
                        #       print(dic1[j])
                        # if "seller"in dic1[j]: #id and link ok
                        #       print(dic1[j+4])
                        # if "seller"in dic1[j]: #name ok
                        #       print(dic1[j+5])
                        # if "additionalProperty" in dic1[j]: #(xuat xu, dia chi) ok
                        #     print(dic1[j+1])
                        # if "seller"in dic1[j]: #type ok
                        #       print(dic1[j+2].replace("@id","").replace(",",""))
                        # if "current_seller"in dic1[j]: 
                        #       print(dic1[j])    
                        # if "other_sellers"in dic1[j]: 
                        #       print(dic1[j])
                        # if "configurable_options"in dic1[j]: 
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
        print("\n\n==============================")
print("+++++++++++++++++++++++++++++++++++++++      DONE ALL              ++++++++++++++++++++++++++++++++++++++++++++++++++")
f.close()
driver.close()
#link seller: //*[@id="__next"]/div[1]/main/div[3]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/a