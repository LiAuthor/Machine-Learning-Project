import os
path = "/home/junkui/SIMI_DATASET"
files = os.listdir(path)
# 变量ｉ用来获取文件名和访问字典的值
i = 0
# 创建提问字典
name={0:"鸡年春联",1:"猴年春联",2:"牛年春联",3:"马牛春联",4:"鼠年春联",5:"兔年春联",6:"羊年春联",7:"蛇年春联",8:"虎年春联",9:"狗年春联",10:"龙年春联",11:"猪年春联"}
# 检查工作路径是否存在文件夹
# PRE_exist=os.path.exists("/home/junkui/SIMI_DATASET/PRE")
# 创建文件夹
os.mkdir("/home/junkui/SIMI_DATASET/PRE")
for file in files:
    file_name = files[i][:-4]
    #判断某个文件名是否存在目标文件夹中
    if not os.path.isdir(file):
        from_file = open(path+"/"+file, 'r')
        #print(file)
        #print(file_name)
        out_file = open("/home/junkui/SIMI_DATASET/PRE"+"/"+file, 'w')
    #out = open('/home/junkui/SIMI_DATASET/shunian_1.yml', 'w')
    #from_file = open('/home/junkui/SIMI_DATASET/shunian.yml', 'r')
        out_file.writelines('categories:')
        out_file.writelines("\n")
        out_file.writelines('- %s' % file_name)
        out_file.writelines("\n")
        out_file.writelines('conversations:')
        out_file.writelines("\n")
        out_file.writelines('- - %s' % name[i])
        out_file.writelines("\n")
        for line in from_file:
            #line是str,强制转换为list
            each_line_list = list(line)
            #if(each_line_list[0])!="\n":
            each_line_list.insert(0, "  - ")
            # print(each_line_list)
            # print(type(each_line_list))
            out_file.writelines("".join(each_line_list))
        out_file.close()
        from_file.close()
    i += 1
