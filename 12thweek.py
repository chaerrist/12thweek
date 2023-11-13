# from bs4 import BeautifulSoup as bs
# import requests as rq


# # url = "https://table.cafe.daum.net/"
# # res = rq.get(url)

# # hmltxt = res.text
# # res_html = bs(hmltxt, 'html.parser')

# # item = res_html.select_one()

# # item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")

# # wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")

# # goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")


# # print(item)
# # print(item.get_text)

# # print(wt)
# # print(wt.get_text)

# # print(goods)
# # print(goods.get_text)

# import os
# from urllib.request import urlretrieve as rl

# url = "https://news.daum.net/"
# res = rq.get(url)

# hmltxt = res.text
# res_html = bs(hmltxt, 'html.parser')

# # # iss = res_html.select("a.wrap_thumb")
# # # print(iss)
# # print("\n--------------------------------------\n")

# # ct = res_html.select("a.wrap_thumb")

# # for j in ct :
# #     c = j.attrs["data-tiara-custom"]
# #     print(c + "\n")

# imgs = res_html.select("img")
# print(imgs)

# linkimgs = []

# for i in imgs :
#     irs = i.attrs["src"]
#     linkimgs.append(irs)

# print(linkimgs)
    
# folder = "imgs/"
# if not os.path.isdir(folder):
#     os.mkdir(folder)
    
# i = 0
# for ln in linkimgs:
#     if str(ln).find("//t") == False :
#         print(ln)
#         continue
#     else:
#         pass
    
#     i += 1
#     rl(ln, folder + f"{i}.jpg")
    
# #import pandas.Series
from pandas import Series as sr
# import numpy as np
    
    
# data - np.arange(5)
data = [10, 20,30, 40]
sdata = sr(data)    

print(sdata)

# # print(sdata.index)
# print(sdata.index.to_list())


sdata.index = ["a", "b", "c", "d"]
print(sdata)