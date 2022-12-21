import time
import io
import csv
from time import sleep
#from matplotlib import image
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
link=[]
with open('tiki_men_lastPage.csv', 'r',encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0]!= "link":
            link.append(row[0])
configurable_options=[]
f=open("reviewCount_tiki_men.txt","w",encoding="utf8")
f.writelines("badges")
for i in range(1,len(link)):
    driver.get(link[i])
    print(link[i])
    print("😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘")
    #f.writelines(link[i]+"\n")
    #f.writelines("😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘😘\n")
    html = driver.find_element_by_tag_name('body')
    for i in range(5):
        html.send_keys(Keys.PAGE_DOWN)
    re1=driver.find_elements_by_xpath("//script[@type='application/ld+json']")
    re=driver.find_elements_by_xpath("//script[@type='application/json']")
    """for i in range (len(re1)):
        if "Product" in re1[i].get_attribute('innerHTML'):            
            dic1=re1[i].get_attribute('innerHTML').split(":[")
            dic2=re1[i].get_attribute('innerHTML').split(",")
            dic3=re1[i].get_attribute('innerHTML').split(":{")
            for j in range(len(dic1)-1):
                # if "Brand" in dic1[j]:
                #     print(dic1[j+1].replace("manufacturer","").replace("}","").replace(",",";")+"\n")
                #     f.writelines(dic1[j+1].replace("manufacturer","").replace("}","").replace(",",";")+"\n")
                # if "sku" in dic1[j]:
                #     #print(dic1[j]+" ủa alo:\n") 
                #     t=dic1[j].split(",")#oke nhen
                #     for k in t:
                #         if "sku" in k:
                #             print(k+"\n")
                #             f.writelines(k+"\n")
                    #print(dic1[j+1].replace("mpn","").replace(",","")+"\n")
                #     f.writelines(dic1[j+1].replace("mpn","").replace(",","")+"\n")
                # if "manufacturer" in dic3[j]:
                #     print(dic3[j+1])
                #     f.writelines(dic3[j+1]+"\n")
                # if "offer" in dic1[j]:           
                #     t=dic1[j+1].split("}")         
                #     print(t[1])
                #     f.writelines(t[0]+"\n")
                # if "aggregateRating"in dic3[j]:
                #     print(dic3[j+1]+"\n")
                #     f.writelines(dic3[j+1]+"\n")
                if "worstRating"in dic2[j]:
                    print(dic2[j]+"\n")
                #     f.writelines(dic2[j]+"\n")
                # if "description"in dic2[j]: #ok
                #     print(dic2[j]+"\n")
                #     f.writelines(dic2[j]+"\n")
                # if "ratingValue"in dic1[j]: 
                #     t=dic1[j].split(",") 
                #     for k in t:
                #         if "ratingValue" in k:
                #             print(k)
                #             f.writelines(k)
                # if "reviewCount"in dic1[j]: 
                #     t=dic1[j].split(",") 
                #     for k in t:
                #         if "reviewCount" in k:
                #             print(k)
                #             f.writelines(k)
                    #f.writelines(dic2[j]+"\n")"""
    for i in range (len(re)):
                dic=re[i].get_attribute('innerHTML')
                dic1=dic.split(",")
                dic2=dic.split(":[{")
                dic3=dic.split(":")
                # for e in range(len(dic3)):
                #     if "categories" in dic3[e]:
                #         print(dic3[e])
                #         f.writelines(dic3[e].replace(",","@")+"\n")
                for d in range(len(dic1)):
                    if "badges" in dic1[d]:
                        print(dic1[j])
                    # if "configurable_options" in dic2[d]: #ok
                    #     #print(dic2[d+1]+" "+dic2[d+2])
                    #     #configurable_options.append(dic2[d+1]+" "+dic2[d+2])
                    #     print(dic2[d+1].replace(",","@")+" "+dic2[d+2]+"\n")
                    #     #f.writelines(dic2[d+1].replace(",","@")+" "+dic2[d+2]+"\n")
                    if "configurable_products" in dic2[d]: #ok
                        #print(dic2[d+1]+" "+dic2[d+2])
                        print(dic2[d+1].replace(",","@")+" "+dic2[d+2].replace(",","@")+"\n")
                        f.writelines(dic2[d+1].replace(",","@")+" "+dic2[d+2].replace(",","@")+"\n")
                for j in range(len(dic1)):
                    # if "master_id" in dic1[j]:#ok
                    #     print(dic1[j].replace(",","@")+"\n")
                    #     f.writelines(dic1[j].replace(",","@")+"\n")
                    # if "url_key"in dic1[j]:#oke nhen
                    #     print(dic1[j].replace(",","@")+"\n")
                    #     f.writelines(dic1[j].replace(",","@")+"\n")
                    # if "discount" in (dic1[j]):#oke nhen
                    #     print(dic1[j].replace(",","@")+"\n")
                    #     f.writelines(dic1[j].replace(",","@")+"\n")
                    # if "review_count"in dic1[j]:
                    #     print(dic1[j].replace(",","@")+"\n")
                    #     f.writelines(dic1[j].replace(",","@")+"\n")
                    # if "thumbnail_url"in dic1[j]: 
                    #     print(dic1[j].replace(",","@")+"\n")
                    #     f.writelines(dic1[j].replace(",","@")+"\n")
                    # if "is_fresh"in dic1[j]:
                    #     print(dic1[j].replace(",","@")+"\n")
                    #     f.writelines(dic1[j].replace(",","@")+"\n")
                    # if "is_flower"in dic1[j]: 
                    #     print(dic1[j].replace(",","@")+"\n")
                    #     f.writelines(dic1[j].replace(",","@")+"\n")
                    # if "is_gift_card"in dic1[j]:
                    #     print(dic1[j].replace(",","@")+"\n")
                    #     f.writelines(dic1[j].replace(",","@")+"\n")
                    # if "data_version"in dic1[j]: 
                    #     print(dic1[j].replace(",","@")+"\n")
                    #     f.writelines(dic1[j].replace(",","@")+"\n")
                    if "is_seller_in_chat_whitelist"in dic1[j]:
                        print(dic1[j].replace(",","@")+"\n")
                        f.writelines(dic1[j].replace(",","@")+"\n")
                    
driver.close()
#f.close()