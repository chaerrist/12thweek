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
    
# # #import pandas.Series
# from pandas import Series as sr
# # import numpy as np
    
    
# # data - np.arange(5)
# data = [10, 20,30, 40]
# sdata = sr(data)    

# print(sdata)

# # # print(sdata.index)
# # print(sdata.index.to_list())


# sdata.index = ["a", "b", "c", "d"]
# print(sdata)

from pandas import Series as sr

# dt = [10, 20,30, 40]
# idx = ["a", "b", "c", "d"]
# # sdata = sr(data)    

# # print(sdata)

# # # sdata.index = ["a", "b", "c", "d"]

# # # sdata = sr(data=idx, index=dt)
# # # sdata - sr(data=dt, index=idx)
# # # sdata = sr(idx, dt)
# # sdata = sr(dt, idx)
# # print(sdata)

# sdata = sr(dt, idx)

# # sd = sdata.reindex["a", "j", "c"]
# # sd = sdata.reindex["a", "c"]
# sd = sdata.reindex["b"]
# print(sd)
# print("\n--------------------------\n")
# print(sdata["b"])

# print(sdata.iloc[0])
# print(sdata.iloc[2])
# print(sdata.iloc["a"])
# print(sdata.iloc["b"])

# # print(sdata[0])

# dt = ["alpha", "beta", "charlie", "delta"]
# idx = ["ab", "bc", "cd", "de"]

# sdata = sr(dt, idx)

# print(sdata.loc["bc" : "cd"])
# print("\n------------------\n")
# print(sdata.loc["bc" : ])
# print("\n------------------\n")
# print(sdata.loc[:"bc"])
# print("\n------------------\n")

# dt = ["사과", "바나나", "수박", "참외"]
# idx = ["가", "나", "다", "라"]

# sdata = sr(data=dt, index=idx)

# print(sdata.iloc[1:2])
# print(sdata.iloc[2:])
# print(sdata.iloc[:2])


# dt = ["alpha", "beta", "charlie", "delta"]
# idx = ["ab", "bc", "cd", "de"]

# sdata = sr(data=dt, index=idx)

# # sdata.loc["cd"] = "echo"
# # print(sdata)
# # sdata.iloc[1] = "fox"
# # print(sdata)

# sdata.drop("bc")
# print(sdata)

# s1 = sr([100, 200, 300], index=["a", "b", "c"])
# s2 = sr([100, 200, 300], index=["b", "c", "a"])

# sum_res = s1 + s2
# print(sum_res)
# print(sum_res.max())
# print(sum_res.min())
# print(sum_res.mean())

# sub_res = s1 - s2
# print(sub_res)
# print(sub_res.max())
# print(sub_res.min())
# print(sub_res.mean())

# mul_res = s2 * 10
# print(mul_res)

# div_res = s1 / 10
# print(div_res)

# data = {
#     "삼성전자": "전기,전자",
#     "LG전자": "전기,전자",
#     "현대차": "운수장비",
#     "NAVER": "서비스업",
#     "카카오": "서비스업"
# }

# sdata = sr(data)
# uniq = sdata.unique()
# print(uniq)

# sc = sdata.count()
# print(sc)

# sv = sdata.value_counts()
# print(sv)

# idx = ["a", "b", "c", "d", "e"]
# s1 = sr([1100, 270, 30, 450, 50], index=idx)
# s2 = sr([150, 740, 810, 40, 25], index=idx)

# # 시리즈내 데이터 비
# fil = s1 > 300
# print(fil)
# print(s1[fil])
# print(s1[fil].index)

# # 시리즈간 비교
# fil1 = s2 > s1
# print(fil1)

# # 인덱싱 출력
# print(s2[s2 > s1].index)

idx = ["a", "b", "c", "d", "e"]
dt = [1100, 270, 30, 450, 50]
s1 = sr(data=dt, index=idx)

sv = s1.sort_values()
print(sv)

sv1 = s1.sort_values(ascending=False)
print(sv1)