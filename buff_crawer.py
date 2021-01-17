"""
网易buff爬虫
Created by Charles-Deng
17jldeng@stu.edu.cn
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}
# cookie
cookie_str = r'Device-Id=18M5mJB9aNR6sROw3Uf3; nts_mail_user=shenej0026@163.com:-1:1; mail_psc_fingerprint=bba38f509eb19ccb5633b2dd363968b7; _ntes_nnid=38e8eaa3a8c419cb6275ed8ad00f2b28,1609842450913; _ntes_nuid=38e8eaa3a8c419cb6275ed8ad00f2b28; Locale-Supported=zh-Hans; game=csgo; _ga=GA1.2.731519374.1610172052; _gid=GA1.2.995557773.1610172052; NTES_YD_SESS=.D5vEGjtx_U8ydt.E8xHwTB9vy4YAcTUbPfTRyB_RD7gmVb8mPEkn1tzPlJLwbiUsFJObY9.kLG0KeKTOCtEO09UCDhZwVmJsBBujHjThtCkp4.jYNxuxQHMoLa9_lZ15Ng..qBBoU_E1.T4PuJetMTYinzlKb7T0E7kyFipJFv_ZPBjlhHW0ht7b7kN1sLOKlDK0d8E2BOrTHaLLyQr3GOHtt0V5mg74p49mVSi4PEKt; S_INFO=1610173594|0|3&80##|17640052174; P_INFO=17640052174|1610173594|1|netease_buff|00&99|hub&1610172518&netease_buff#hub&420100#10#0#0|&0|null|17640052174; remember_me=U1092088919|3tiLfJqOhfBYdZJI5RvlYBnFE5IXpCA4; session=1-UxyAZflStZf4-hpza9jAix0JLzBR-cpVf_iSCLn0eHXJ2044291855; _gat_gtag_UA_109989484_1=1; csrf_token=IjdiY2ViMTNkZDFhNjQ0NTJhMmRmMmQzYWQ4ZmMyOGIxOGNkMmRkMjEi.EtreHA.9A43kbAOqH0385ppA8Gqt0ClAqs'
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value


import numpy as np
import pandas as pd
import time
import csv
import re
import requests
import Crawer_v1
from collections import Counter
import random
import itertools as its

begin = time.time()

with open('items_sorting2.csv', 'r', encoding = "UTF-8") as f1:
    reader1 = csv.reader(f1)
    result1 = list(reader1)
temple_dic = {}
for row in result1:
    temple_dic[row[1]] = [row[2], row[3], row[4], row[5]]
del temple_dic["id"]
main_ST_dic = {}
main_dic1 = {}
temple_dic2 = {}
for key in temple_dic.keys():
    if "纪念品" not in temple_dic[key][0]:
        temple_dic2[key] = temple_dic[key]
temple_dic = temple_dic2
for key in temple_dic.keys():
    if "StatTrak" in temple_dic[key][0]:
        main_ST_dic[key] = temple_dic[key]
    else:
        main_dic1[key] = temple_dic[key]
main_dic1['776411'] = ['SSG 08 | 喋血战士 (略有磨损)_CS:GO','裂网大行动','保密','134']

boxes_set = set([x[1] for x in main_dic1.values()])
boxed_list = list(boxes_set)
rarity_set = set([x[2] for x in main_dic1.values()])
rarity_list = list(rarity_set)
# 分等级
for key in main_dic1.keys():
    if main_dic1[key][2] == "消费":
        main_dic1[key][2] = 1
    elif main_dic1[key][2] == "工业":
        main_dic1[key][2] = 2
    elif main_dic1[key][2] == "军规":
        main_dic1[key][2] = 3
    elif main_dic1[key][2] == "受限":
        main_dic1[key][2] = 4
    elif main_dic1[key][2] == "保密":
        main_dic1[key][2] = 5
    elif main_dic1[key][2] == "隐秘":
        main_dic1[key][2] = 6
# 同一等级中找十个箱子
for i in range(1,6):
    pass
# 用于存放当前等级的物品
temp_dic = {}
i = 4
for key in main_dic1.keys():
    if main_dic1[key][2] == i: # 保密到隐秘的炼金(改为i)
        temp_dic[key] = main_dic1[key]
# 等级4中ban list: 运河水城，棱镜
temple_dic = {}
for key in main_dic1.keys():
    if main_dic1[key][1] != "运河水城":
        temple_dic[key] = main_dic1[key]
main_dic1 = {}
for key in temple_dic.keys():
    if temple_dic[key][1] != "棱镜":
        main_dic1[key] = temple_dic[key]

# 用于存放下一等级的物品
next_dic = {}
for key in main_dic1.keys():
    if main_dic1[key][2] == i+1: # 保密到隐秘的炼金(改为i+1)
        next_dic[key] = main_dic1[key]
# 用于存放当前等级可供选择的物品
items_list = []
for key in temp_dic.keys():
    items_list = items_list + [[key,temp_dic[key][0],temp_dic[key][1],temp_dic[key][2],temp_dic[key][3]]]

# 穷举出所有可能
# for a in range(len(items_list)):
#     for b in range(len(items_list)):
#         for c in range(len(items_list)):
#             for d in range(len(items_list)):
#                 for e in range(len(items_list)):
#                     for f in range(len(items_list)):
#                         for g in range(len(items_list)):
#                             for h in range(len(items_list)):
#                                 for x in range(len(items_list)):
#                                     for y in range(len(items_list)):
#                                         print(a,b,c,d,e,f,g,h,x,y)
#                                         choices_list = [items_list[a], items_list[b], items_list[c],
#                                         items_list[d], items_list[e],items_list[f],items_list[g],
#                                         items_list[h], items_list[x], items_list[y]]
#   for (a,b,c) in z 向量化处理
while True:
    try:
        # choices_list = random.choices(items_list, k=10)
        choices_list = [['775084', 'MP7 | 七彩斑斓 (崭新出厂)', '裂网大行动', 4, '15']] * 10
        cost = 0
        gain = []
        gain_dic = {}
        for o in range(10):
            cost = cost + float(choices_list[o][4])
            box_beloning = choices_list[o][2]
            # 计算可能获得的物件数，作除数
            count = 0
            gain0 = 0
            for key in next_dic.keys():
                if next_dic[key][1] == box_beloning:
                    gain0 = gain0 + (float(next_dic[key][3]))
                    count = count + 1
                    gain_dic[key] = next_dic[key]
            gain0 = gain0 / (count * 10)
            gain0 = round(gain0,1)
            gain.append(gain0)
        gain_num = 0

        for get in gain:
            gain_num = gain_num + get
        # if gain_num  < cost +10  :
        #     continue
        # else:

        break
    except(ZeroDivisionError):
        continue
print("cost",cost)
print("gain",gain_num)
print("std",np.std(gain))




                                                        # boxes_list = list(boxes_set)
"""
with open('items_sorting.csv', 'r', encoding = "UTF-8") as f1:
    reader1 = csv.reader(f1)
    result1 = list(reader1)
with open('items_information.csv', 'r', encoding = "UTF-8") as f2:
    reader2 = csv.reader(f2)
    result2 = list(reader2)
# 处理行信息
temp_dic1 = {}
temp_dic2 = {}
for row in result1:
    temp_dic1[row[1]] = [row[2], row[3], row[4]]
for row in result2:
    temp_dic2[row[1]] = [row[2], row[3]]
for key in temp_dic1.keys():
    temp_dic1[key].append(temp_dic2[key][1])
del temp_dic1["id"]
name = ["id", "Chinese_name", 'belonging', "type", "price"]
data = zip(list(temp_dic1.keys()), [x[0] for x in list(temp_dic1.values())],
           [x[1] for x in list(temp_dic1.values())]
           , [x[2] for x in list(temp_dic1.values())],[x[3] for x in list(temp_dic1.values())])
items_sorting = pd.DataFrame(columns=name, data=data)
items_sorting.to_csv("items_sorting2.csv")
"""

end = time.time()
print(end - begin)
