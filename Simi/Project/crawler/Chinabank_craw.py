import requests
from urllib.request import urlopen
import re
import json
from bs4 import BeautifulSoup
# All_Ajax_link = urlopen(
#    "https://95566.boc.cn/mgw4msg/v1/robot/web/common_knowledge_catalogue?_=1570778312352").read().decode('utf-8')
# "https://95566.boc.cn/mgw4msg/v1/robot/web/common_knowledge?catalogueId=77C734421A1F4FF6E053B20C0B16F49A&accessChannelCode=JRQD1-MHWZ&_=1670798098408").read().decode()
# print(All_Ajax_link)
# number = json.loads(All_Ajax_link)
# print(json.loads(All_Ajax_link))


# 第一步获取问题列表的全部Ajax请求码，正则提取出来并将其写入列表
with open('./China_bank', 'r') as f:
    str_china_bank = f.read()
pattern = re.compile("\"catalogueId\"\:\"(.+?)\"\,\"catalogueName", re.S)
results = re.findall(pattern, str_china_bank)
print(len(results))
# 创建列表存储父亲问题的Ajax_link
All_Ajax_link_list = []
for i in range(len(results)):
    # 创建父亲问题的完整Ajax_link
    temp = "https://95566.boc.cn/mgw4msg/v1/robot/web/common_knowledge?catalogueId=" + \
        results[i]+"&accessChannelCode=JRQD1-MHWZ"
    All_Ajax_link_list.append(temp)
# print(All_Ajax_link_list)

out_file = open('./bank_FAQ_1.yml', 'w')
out_file.writelines('categories:')
out_file.writelines("\n")
out_file.writelines('- ChinaBankFAQ')
out_file.writelines("\n")
out_file.writelines('conversations:')
out_file.writelines("\n")
# 遍历访问所有父亲问题
for i in range(len(All_Ajax_link_list)):
    if(i != 38 or i != 39):
        # 首先请求得到网页json数据,然后解析
        each_ajax_link_json = urlopen(All_Ajax_link_list[i]).read().decode()
        json_dict = json.loads(each_ajax_link_json)
        for item in json_dict['common_knowledge_list']:

            #print("%s\n%s\n" % (item['standQues'], item['answer']))
            out_file.writelines("- - %s" % item['standQues'])
            out_file.writelines("\n")
            out_file.writelines("  - %s" % item['answer'].replace('\n', ''))
            out_file.writelines("\n")
        print("问题:%d 写入成功" % i)
    else:
        print("问题:%d 已经过滤" % i)
out_file.close()
