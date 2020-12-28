import re
import requests

'''
# 爬取一级页面的链接


def get_link(response):
    # 正则表达式
    pattern = re.compile('<span><a.*?\=\"(.*?)\".*?get')
    results = re.findall(pattern, response.text)
    # print(type(results))
    # print(len(results))
    # 添加头链接
    link_len = len(results)
    head_link = "https://so.gushiwen.org"
    for i in range(link_len):
        results[i] = head_link+results[i]
    # print(len(results))
    return results


# 爬取二级页面的内容
def get_data(results):
    pattern = re.compile(
        '<h1.*?bottom.*?\">(.*?)</h1>.*?aspx\"(.*?)</a>.*?class\">(.*?)</div>')
    data = []
    for i in range(len(results)):
        data[i] = re.findall(pattern, results[i])
    print(data)
    return

'''
# 正则表达式
response = requests.get("https://so.gushiwen.org/gushi/tangshi.aspx")
pattern = re.compile('<span><a.*?\=\"(.*?)\".*?get')
results = re.findall(pattern, response.text)
link_len = len(results)
head_link = "https://so.gushiwen.org"
data = []
for i in range(link_len):
    results[i] = head_link+results[i]
    # print(results[i])
    link = requests.get(results[i])
    pattern_data = re.compile(
        '<h1.*?bottom.*?10px;\">(.*?)</h1>.*?aspx\">(.*?)</a>.*?class.*?\">(.*?)</div>', re.S)
    every_data = re.findall(pattern_data, link.text)
    # print(every_data[0])
    # print(type(every_data[0][2]))
    # temp_every_data = re.sub('<br />', '', every_data[0][2])
    # print(type(temp_every_data))
    # print(every_data[0][2])
    data.append(every_data[0])
    # print(type(every_data[0]))
# print(data)
with open('../corpus/shiming_1.yml', 'w') as f:
    for i in range(len(data)):
        f.write('- - ')
        f.write(data[i][0])
        f.write('\n')
        f.write('  - 作者：')
        f.write(data[i][1])
        f.write(re.sub('<br />', '', data[i][2]))


# open('shiming.yml', 'w').write(
#   '\n'.join('%s\n%s' % x for x in data))
