# -*- coding: utf-8 -*-
#   网易buff爬虫

import requests
import re
import time
import numpy as np
import pandas as pd
import csv
from bs4 import BeautifulSoup
import pickle

# # 写入文档
# with open('./origin_page.html', 'w', encoding='utf-8') as fp:
#     fp.write(html_text0)
sleeptime = 1
def initialization():   # 初始化头信息即cookies
    global headers
    global cookies
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }
    # cookie
    cookie_str = r'Device-Id=18M5mJB9aNR6sROw3Uf3; nts_mail_user=shenej0026@163.com:-1:1; mail_psc_fingerprint=bba38f509eb19ccb5633b2dd363968b7; _ntes_nnid=38e8eaa3a8c419cb6275ed8ad00f2b28,1609842450913; _ntes_nuid=38e8eaa3a8c419cb6275ed8ad00f2b28; _ga=GA1.2.731519374.1610172052; Locale-Supported=zh-Hans; game=csgo; _gid=GA1.2.129018010.1610765726; NTES_YD_SESS=WUoZdKZ_c4RXob.EQQ3TAK7HZ.xxpd9MdUURx6fdV3K5n8oQh01DuZxK2jFHq2qCaIxrN.UXbN1XAEYc0zlTIW2LxxN9mSNxgv9Di5J0eafOiY604Yx1arZJuV3e5YoX0zPh9ieHsQi5p4xoGiVGX0KA2q_hjE4z4xGmO5YdE.0oNq_vvrVc8fxy82DcFAjOfNaG_Kd_laTxIoNXZz2LUXS7dqPtpTV6Zewax2kgZRRYA; S_INFO=1610788702|0|3&80##|1-5416042391; P_INFO=1-5416042391|1610788702|1|netease_buff|00&99|null&null&null#hub&420100#10#0|&0|null|1-5416042391; remember_me=U1098626453|iLh5iXzc3KEvgAV4Cdkq8X8LpvGVkUte; session=1-3aC3gpNQgfwauVRC8x7J4xoaG1U1lwQuoqwFc7cDlBK62041916109; _gat_gtag_UA_109989484_1=1; csrf_token=ImJhM2ExMzU0NTgxZWI3NGYwOGM1N2ExNjBkNzNkODhhNWQ0ZTQxMjgi.EuRA4g.4GUxnY0sCyrzSlrjqsJc5WA5ims'
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
def get_category(): # 获取category
    global category_list
    # Buff csgo武器页面源代码
    source_page_url = "https://buff.163.com/market/?game=csgo#tab=selling&page_num=1"
    cat_response = requests.get(url=source_page_url, headers=headers, cookies=cookies)
    html_text0 = cat_response.text
    soup = BeautifulSoup(html_text0,'lxml')
    # 找出各个武器种类
    category_list = re.findall( r'li value="weapon_(.+?)">', html_text0, re.M)
    for i in range(len(category_list)):
        category_list[i] = "weapon_" + category_list[i]
def decode_pages(): # 解析网页
    # 物品名字
    names_list = []
    # 物品价格
    price_list = []
    # id
    id_list = []
    # 指定蝴蝶刀界面“https://buff.163.com/market/?game=csgo#tab=selling&page_num=1&category=weapon_knife_butterfly”
    root_url = 'https://buff.163.com/api/market/goods?game=csgo&'
    for i in range(len(category_list)):
        # 获取不同物件名称
        # 标准url：https://buff.163.com/api/market/goods?game=csgo&page_num=1&category=weapon_knife_butterfly
        category_url = "&category=" + category_list[i]
        first_url = 'https://buff.163.com/api/market/goods?game=csgo&page_num=1' + category_url
        # 获取单一物件的总页码
        page_response = requests.get(url=first_url, headers=headers, cookies=cookies)
        html_text1 = page_response.text
        page_num_list = re.findall(r'"total_page": (.*)', html_text1, re.M)
        if page_num_list != []:
            page_num = page_num_list[0]
        time.sleep(sleeptime)
        # 获取单一物件每一页的信息
        for page in range(1, int(page_num) + 1):
            time.sleep(sleeptime*2)
            page_str = 'page_num=' + str(page)
            # 合并成新的url
            url = root_url + page_str + category_url
            detail_response = requests.get(url=url, headers=headers, cookies=cookies)
            html_text2 = detail_response.text
            # 获取名字和价格
            names_list_temp = re.findall(r'"market_hash_name": "(.*)",', html_text2, re.M)
            price_list_temp = re.findall(r'"sell_min_price": "(.*)",', html_text2, re.M)
            id_list_temp = re.findall(r'"id": (.*),', html_text2, re.M)
            # 异常处理
            if names_list_temp == [] or price_list_temp == [] or id_list_temp == []:
                lost_page = page
                lost_catergory = category_list[i]
                lost_text = "Lost in page:" + str(lost_page) + "of category:" + lost_catergory
                with open('wrong.txt', 'w', encoding='utf-8') as fp:
                    fp.write(lost_text)

            names_list = names_list + names_list_temp
            price_list = price_list + price_list_temp
            id_list = id_list + id_list_temp
        for i in range(len(names_list)):
            print(names_list[i] + ':' + price_list[i])
    # 汇合信息写成表格并保存
    csv_name = ["id","name","price"]
    csv_data = zip(id_list,names_list,price_list)
    items_information = pd.DataFrame(columns=csv_name, data=list(csv_data))
    items_information.to_csv("items_information.csv")
def boxes_sorting():
    with open('items_information.csv', 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    temp_dic = {}
    main_dic = {}
    # 处理行信息
    for row in result:
        temp_dic[row[1]] = [row[2], row[3]]
    for key in temp_dic.keys():
        if '\\u2605' not in temp_dic[key][0]:
            main_dic[key] = temp_dic[key]
    # 崭新出厂
    fac_new_dic = {}
    for key in main_dic.keys():
        if 'Factory New' in main_dic[key][0]:
            fac_new_dic[key] = main_dic[key]
    fac_new_all_dic = fac_new_dic
    # 略磨
    fac_lm_dic = {}
    for key in main_dic.keys():
        if 'Minimal Wear' in main_dic[key][0]:
            fac_lm_dic[key] = main_dic[key]
    fac_lm_all_dic = fac_lm_dic
    # 酒精
    fac_jj_dic = {}
    for key in main_dic.keys():
        if 'Field-Tested' in main_dic[key][0]:
            fac_jj_dic[key] = main_dic[key]
    fac_jj_all_dic = fac_jj_dic
    # statTrack 崭新
    fac_new_dic = {}
    fac_new_st_dic = {}
    for key in fac_new_all_dic.keys():
        if 'StatTrak\\u2122' in fac_new_all_dic[key][0]:
            fac_new_st_dic[key] = fac_new_all_dic[key]
        else:
            fac_new_dic[key] = fac_new_all_dic[key]
    # statTrack 略磨
    fac_lm_dic = {}
    fac_lm_st_dic = {}
    for key in fac_lm_all_dic.keys():
        if 'StatTrak\\u2122' in fac_lm_all_dic[key][0]:
            fac_lm_st_dic[key] = fac_lm_all_dic[key]
        else:
            fac_lm_dic[key] = fac_lm_all_dic[key]
    # statTrack 酒精
    fac_jj_dic = {}
    fac_jj_st_dic = {}
    for key in fac_jj_all_dic.keys():
        if 'StatTrak\\u2122' in fac_jj_all_dic[key][0]:
            fac_jj_st_dic[key] = fac_jj_all_dic[key]
        else:
            fac_jj_dic[key] = fac_jj_all_dic[key]

    fac_all_dic = {}
    fac_all_dic.update(fac_new_all_dic)
    fac_all_dic.update(fac_lm_all_dic)
    fac_all_dic.update(fac_jj_all_dic)


    print(fac_lm_all_dic)
    standard_url = "https://buff.163.com/market/goods?goods_id=39954&from=market"
    root_url = "https://buff.163.com/market/goods?goods_id="
    tail_url = "&from=market"
    box_sort_dic = {}
    items_type = ["消费", "工业", "军规", "受限", "保密", "隐秘"]

    for id in list(fac_all_dic.keys()):
        time.sleep(sleeptime)
        sort_url = root_url + id + tail_url
        sort_response = requests.get(url=sort_url, headers=headers, cookies=cookies)
        html_text4 = sort_response.text
        # 找出各个武器的中文名字
        chinese_list = re.findall(r'<head><title>(.*?)_CS:GO饰品交易', html_text4, re.M)
        print(chinese_list)
        # 找出所属箱子
        box_list = re.findall(r',(.*?)收藏品,', html_text4, re.M)
        if box_list == []:
            box_list = re.findall(r',(.*?)collection,', html_text4, re.M)
        # 判断稀有度
        for str in items_type:
            if str in html_text4:
                type_str = str
                break
            else:
                if items_type.index(str) == len(items_type):
                    type_str = "Na"
                    print("type error occurd in id:" + id)
                else:
                    continue
        try:
            if len(box_list[0]) > 19:
                tstr = box_list[0]
                box_list[0] = tstr.split(",")[-1]
        except(IndexError):
            pass
        if box_list == []:
            print("box_list empty occurd in id:" + id)
            box_sort_dic[id] = [chinese_list[0], ["Na"], type_str]
            continue
        box_sort_dic[id] = [chinese_list[0], box_list[0], type_str]
        print(id)
        print(box_sort_dic[id])
    with open('data.pkl', 'wb') as fp:
        pickle.dump(box_sort_dic, fp, pickle.HIGHEST_PROTOCOL)
    with open('items_information.csv', 'r', encoding="UTF-8") as f2:
        reader2 = csv.reader(f2)
        result2 = list(reader2)
    temp_dic2 = {}
    for row in result2:
        temp_dic2[row[1]] = [row[2], row[3]]
    for key in box_sort_dic.keys():
        box_sort_dic[key].append(temp_dic2[key][1])

    name = ["id", "Chinese_name", 'belonging', "type", "price"]
    data = zip(list(box_sort_dic.keys()), [x[0] for x in list(box_sort_dic.values())],
               [x[1] for x in list(box_sort_dic.values())]
               , [x[2] for x in list(box_sort_dic.values())], [x[3] for x in list(box_sort_dic.values())])
    items_sorting = pd.DataFrame(columns=name, data=list(data))
    items_sorting.to_csv("items_sorting.csv")


if __name__ == '__main__':
    start_time = time.time()
    initialization()    # 初始化
    get_category()      # 获取目录
    # decode_pages()      # 解码页面，获取csv
    boxes_sorting()        # 武器分类
    # get_history_price()   # 获取历史价格
    # his_pri_analyze()     # 分析历史价格（待完善）

    end_time = time.time()
    dtime = end_time-start_time
    print("spending time:"+str(dtime))





