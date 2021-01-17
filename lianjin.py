import pickle
import pandas as pd
import csv
from random import choice
with open('lianjin.txt', 'w+') as fl:
    fl.close()

with open('data.pkl', 'rb+') as f:
    box_sort_dic = pickle.load(f, encoding='iso-8859-1')

with open('items_information.csv', 'r', encoding="UTF-8") as f2:
    reader2 = csv.reader(f2)
    result2 = list(reader2)
temp_dic2 = {}
for row in result2:
    temp_dic2[row[1]] = [row[2], row[3]]
for key in box_sort_dic.keys():
    box_sort_dic[key].append(temp_dic2[key][1])
box_sort_dic['38839'][2] = '隐秘'
box_sort_dic['35240'][2] = '隐秘'
box_sort_dic['38841'][2] = '隐秘'
box_sort_dic['35239'][2] = '隐秘'
box_sort_dic['38840'][2] = '隐秘'
box_sort_dic['35238'][2] = '隐秘'
box_sort_dic['763254'][2] = '保密'
box_sort_dic['763256'][2] = '保密'
box_sort_dic['763419'][2] = '保密'
box_sort_dic['763426'][2] = '保密'
box_sort_dic['34658'][2] = '保密'
box_sort_dic['34656'][2] = '保密'
box_sort_dic['38516'][2] = '保密'
box_sort_dic['38518'][2] = '保密'
box_sort_dic['763254'][2] = '保密'
box_sort_dic['763289'][2] = '保密'
box_sort_dic['763382'][2] = '保密'
box_sort_dic['38517'][2] = '保密'
box_sort_dic['34657'][2] = '保密'
#print(box_sort_dic) #'39205': ['P2000（StatTrak™） | 至尊威龙 (崭新出厂)', '伽玛', '保密', '80'],
ShouCangPin = {}

for id in box_sort_dic.keys():
    # print(id)
    # print(box_sort_dic[id])
    if not isinstance(box_sort_dic[id][1], list):
        ShouCangPin[box_sort_dic[id][1]] = []


for id in box_sort_dic.keys():
    if not isinstance(box_sort_dic[id][1], list):
        if box_sort_dic[id][0].split(' (')[0] not in ShouCangPin[box_sort_dic[id][1]]:
            ShouCangPin[box_sort_dic[id][1]].append([box_sort_dic[id][0].split(' (')[0], box_sort_dic[id][2]])
for key in ShouCangPin.keys():
    temp = []
    for item in ShouCangPin[key]:
        if not item in temp:
            temp.append(item)
    ShouCangPin[key] = temp
print(ShouCangPin)

items_type = ["消费", "工业", "军规", "受限", "保密", "隐秘"]

# for i in ShouCangPin['伽玛']:
#     print(i)
#print(ShouCangPin) #'伽玛': [['P2000（StatTrak™） | 至尊威龙', '保密'], ['P2000 | 至尊威龙', '保密'],
xiyoudu = {}
clscp = []
mosun_region = [0.05,0.06,0.07,0.08,0.09,0.10,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.30,0.31,0.32,0.33,0.34,0.35,0.36,0.37]
print(mosun_region)
for id in box_sort_dic.keys():
    # print(id)
    # print(box_sort_dic[id])
    xiyoudu[box_sort_dic[id][2]] = []


for id in box_sort_dic.keys():
    if box_sort_dic[id][0].split(' (')[0] not in xiyoudu[box_sort_dic[id][2]]:
        xiyoudu[box_sort_dic[id][2]].append([box_sort_dic[id][0].split(' (')[0], box_sort_dic[id][1]])
#print(xiyoudu)  #'保密': [['P2000（StatTrak™） | 至尊威龙', '伽玛'], ['P2000 | 至尊威龙', '伽玛'],

#材料列表
cl = []
#添加材料

def addCL():
    global itemType
    global target_rare
    global isStatTrak
    global cl
    # for i in range(5):
    #     cl.append('M4A4 | 地狱烈焰')
    # for i in range(5):
    #     cl.append('P2000 | 珊瑚树')
    mosun = [0 for i in range(10)]
    print(xiyoudu['保密'])
    cl_all_list = []
    cl_mosun = []
    cl = [i for i in range(10)]
    for xyd in xiyoudu.keys():
        if xyd == '保密':
            for item_xyd in xiyoudu[xyd]:
                cl[0] = item_xyd[0]
                for item_xyd in xiyoudu[xyd]:
                    cl[1] = item_xyd[0]
                    for item_xyd in xiyoudu[xyd]:
                        cl[2] = item_xyd[0]
                        for item_xyd in xiyoudu[xyd]:
                            cl[3] = item_xyd[0]
                            for item_xyd in xiyoudu[xyd]:
                                cl[4] = item_xyd[0]
                                for item_xyd in xiyoudu[xyd]:
                                    cl[5] = item_xyd[0]
                                    for item_xyd in xiyoudu[xyd]:
                                        cl[6] = item_xyd[0]
                                        for item_xyd in xiyoudu[xyd]:
                                            cl[7] = item_xyd[0]
                                            for item_xyd in xiyoudu[xyd]:
                                                cl[8] = item_xyd[0]
                                                for item_xyd in xiyoudu[xyd]:
                                                    cl[9] = item_xyd[0]
                                                    mosun = [0.05 for i in range(10)]
                                                    for i in range(len(cl)):
                                                        cl_mosun.append([cl[i], mosun[i]])
                                                    cl_all_list.append(cl.copy())
                                                    search = cl[0]
                                                    for id in box_sort_dic.keys():
                                                        if box_sort_dic[id][0].startswith(search):
                                                            itemType = box_sort_dic[id][2]
                                                    # 判断是不是暗金
                                                    flag = 1
                                                    if '（StatTrak™）' in cl[0]:
                                                        isStatTrak = True
                                                        for i in cl:
                                                            if '（StatTrak™）' not in i:
                                                                flag = 0
                                                    else:
                                                        isStatTrak = False
                                                        for i in cl:
                                                            if '（StatTrak™）' in i:
                                                                flag = 0
                                                    if flag:

                                                        target_rare = items_type[items_type.index(itemType) + 1]
                                                        # getClScp()
                                                        clscp = []
                                                        for clItem in cl:
                                                            for key in xiyoudu.keys():
                                                                for item in xiyoudu[key]:
                                                                    if clItem in item:
                                                                        clscp.append(item[1])
                                                                        break
                                                        # getTarget()
                                                        target_dic = {}
                                                        for clscpItem in clscp:
                                                            if not isinstance(clscpItem, list):
                                                                for scpitem in ShouCangPin[clscpItem]:
                                                                    if isStatTrak:
                                                                        if '（StatTrak™）' in scpitem[0] and '纪念品' not in scpitem[0] and scpitem[1] == target_rare:
                                                                            if scpitem[0] in target_dic.keys():
                                                                                target_dic[scpitem[0]] += 1
                                                                            else:
                                                                                target_dic[scpitem[0]] = 1
                                                                    else:
                                                                        if '（StatTrak™）' not in scpitem[0] and '纪念品' not in scpitem[0] and scpitem[1] == target_rare:
                                                                            if scpitem[0] in target_dic.keys():
                                                                                target_dic[scpitem[0]] += 1
                                                                            else:
                                                                                target_dic[scpitem[0]] = 1
                                                            else:
                                                                print('这组不算')
                                                                break
                                                        # printTarget()

                                                        count = 0
                                                        price = 0
                                                        target_list = []

                                                        chengben = 0
                                                        cl2 = cl.copy()
                                                        for i in range(len(cl2)):
                                                            cl2[i] += ' (崭新出厂)'
                                                        print(cl2)
                                                        for item in cl2:
                                                            for value in box_sort_dic.values():
                                                                if item == value[0]:
                                                                    chengben += float(value[3])

                                                        for key in target_dic.keys():
                                                            count += target_dic[key]
                                                            target_list.append(key)
                                                        for i in range(len(target_list)):
                                                            target_list[i] += ' (崭新出厂)'
                                                        print(target_dic)
                                                        price_list = [0 for i in range(100)]
                                                        for i in range(len(target_list)):
                                                            for value in box_sort_dic.values():
                                                                if target_list[i] == value[0]:
                                                                    # if len(value) < 4:
                                                                    #     value[3] = 0
                                                                    #     print('这条有问题！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
                                                                    price_list[i] = float(value[3])
                                                        print(price_list)
                                                        i = 0
                                                        for key, value in target_dic.items():
                                                            price += value / count * price_list[i]
                                                            i += 1
                                                        for i in cl:
                                                            if '纪念品' in i:
                                                                chengben = 9999999
                                                        profit = price - chengben
                                                        profit_rate = profit / chengben
                                                        if chengben < price:
                                                            with open('lianjin.txt', 'a') as fla:
                                                                fla.writelines('当前炼金材料：' + '\n')
                                                                for i in cl:
                                                                    fla.writelines(i + '\n')
                                                                fla.writelines('当前炼金稀有度:' + itemType + '\n')
                                                                fla.writelines('出货稀有度:' + target_rare + '\n')
                                                                fla.close()
                                                            print('当前炼金材料：')
                                                            for i in cl:
                                                                print(i)
                                                            print('当前炼金稀有度:' + itemType)
                                                            # target_rare = items_type[items_type.index(itemType) + 1]
                                                            print('出货稀有度:' + target_rare)
                                                            with open('lianjin.txt', 'a') as fla:
                                                                fla.writelines('出货列表：' + '\n')
                                                            print('出货列表：')
                                                            for key, value in target_dic.items():
                                                                with open('lianjin.txt', 'a') as fla:
                                                                    fla.writelines(
                                                                        key + ':' + str(value / count) + '\n')
                                                                print(key + ':' + str(value / count))
                                                            with open('lianjin.txt', 'a') as fla:
                                                                fla.writelines('成本：' + str(chengben) + '\n')
                                                                fla.writelines('期望：' + str(price) + '\n')
                                                                fla.writelines('赚：' + str(profit) + '   ' + str(
                                                                    profit_rate) + '\n')
                                                                fla.writelines("  " + '\n')
                                                                fla.writelines("========================================================" + '\n')
                                                                fla.writelines("  " + '\n')
                                                            print('成本：' + str(chengben))
                                                            print('期望：' + str(price))
                                                            print('赚：' + str(profit) + '   ' + str(profit_rate))

                                                            print("  ")
                                                            print("========================================================")
                                                            print("  ")
    # cl = ['AUG | 席德.米德', 'AUG | 燕群', 'AWP | 石墨黑', 'AWP | 石墨黑', 'AWP | 石墨黑', 'AWP | 石墨黑', 'AWP | 石墨黑', 'AWP | 石墨黑', 'AWP | 石墨黑','AWP | 石墨黑']
    # # for item_xyd in xiyoudu[xyd]:
    # #     for i in range(len(cl)):
    # #         cl[i] = item_xyd[0]
    # #     for i in range(len(mosun)):
    # #         mosun[i] = mosun_region[i]
    # #     cl_dic = {}
    # #     for i in range(len(cl)):
    # #         cl_dic[cl[i]] = mosun[i]
    # #     cl_all_list.append(cl_dic)
    # #     print(cl_all_list)
    # search = cl[0]
    # for id in box_sort_dic.keys():
    #     if box_sort_dic[id][0].startswith(search):
    #        itemType = box_sort_dic[id][2]
    # # 判断是不是暗金
    # if '（StatTrak™）' in cl[0]:
    #     isStatTrak = True
    # else:
    #     isStatTrak = False
    # print('当前炼金材料：')
    # for i in cl:
    #     print(i)
    # print('当前炼金稀有度:' + itemType)
    # target_rare = items_type[items_type.index(itemType) + 1]
    # print('出货稀有度:' + target_rare)
    # getClScp()
    # getTarget()




def getTarget():
    global target_dic
    global clscp
    print(clscp)
    target_dic = {}
    for clscpItem in clscp:
        if not isinstance(clscpItem,list):
            for scpitem in ShouCangPin[clscpItem]:
                if isStatTrak:
                    if '（StatTrak™）' in scpitem[0] and scpitem[1] == target_rare:
                        if scpitem[0] in target_dic.keys():
                            target_dic[scpitem[0]] += 1
                        else:
                            target_dic[scpitem[0]] = 1
                else:
                    if '（StatTrak™）' not in scpitem[0] and scpitem[1] == target_rare:
                        if scpitem[0] in target_dic.keys():
                            target_dic[scpitem[0]] += 1
                        else:
                            target_dic[scpitem[0]] = 1
        else:
            with open('lianjin.txt', 'a') as fla:
                fla.write('这组不算' + '\n')
                fla.close()
            print('这组不算')
            return
    printTarget()

def printTarget():
    global target_dic
    global cl
    with open('lianjin.txt', 'a') as fla:
        fla.writelines('出货列表：' + '\n')
    print('出货列表：')
    count = 0
    price = 0
    target_list = []

    chengben = 0
    cl2 = cl.copy()
    for i in range(len(cl2)):
        cl2[i] += ' (崭新出厂)'
    print(cl2)
    for item in cl2:
        for value in box_sort_dic.values():
            if item == value[0]:
                chengben += float(value[3])


    for key in target_dic.keys():
        count += target_dic[key]
        target_list.append(key)
    for i in range(len(target_list)):
        target_list[i] += ' (崭新出厂)'
    print(target_dic)
    price_list = [0 for i in range(100)]
    for i in range(len(target_list)):
        for value in box_sort_dic.values():
            if target_list[i] == value[0]:
                # if len(value) < 4:
                #     value[3] = 0
                #     print('这条有问题！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
                price_list[i] = float(value[3])
    print(price_list)
    i = 0
    for key,value in target_dic.items():
        with open('lianjin.txt', 'a') as fla:
            fla.writelines(key + ':' + str(value/count) + '\n')
        print(key + ':' + str(value/count))
        price += value/count * price_list[i]
        i += 1

    profit = price - chengben
    profit_rate = profit/chengben
    if chengben < price:
        with open('lianjin.txt', 'a') as fla:
            fla.writelines('成本：'+str(chengben) + '\n')
            fla.writelines('期望：'+str(price) + '\n')
            fla.writelines('赚：' + str(profit) + '   ' + str(profit_rate) + '\n')
            fla.writelines("  " + '\n')
            fla.writelines("========================================================" + '\n')
            fla.writelines("  " + '\n')
        print('成本：'+str(chengben))
        print('期望：'+str(price))
        print('赚：'+ str(profit) + '   ' + str(profit_rate))

        print("  ")
        print("========================================================")
        print("  ")
def getClScp():
    global clscp
    global cl
    clscp = []
    for clItem in cl:
        for key in xiyoudu.keys():
            for item in xiyoudu[key]:
                if clItem in item:
                    clscp.append(item[1])
                    break
def run():
    addCL()   #添加材料
    #getClScp()   #识别材料所属收藏品

if __name__ == '__main__':
    run()