# 导入词库和要提取的文章，并转换成列表

from doctest import DONT_ACCEPT_BLANKLINE
from clean_docs import clean_doc 
from initializing_process import clean_doc, initializing_doc_main

# 用户输入方式获取生词位置

input_file_name = input("\n请输入生词文件名称（不要包含扩展名）：")
obj_path = "C:\\Users\\bowen\\Desktop\\" + input_file_name + ".txt"

# 获取初始化的文件

basic_list = initializing_doc_main("熟词库.txt")
basic_list = set(basic_list)
basic_list = list(basic_list)
basic_list = sorted(basic_list)
obj_list = initializing_doc_main(obj_path)

# 粗过滤

shengci_list = []
shuci_list = []

for word in obj_list:
    if word in basic_list:
        shuci_list.append(word.lower())
    else:
        shengci_list.append(word.lower())


"""
处理生词
"""


# 统计生词频率

shengci_freq = {}

# 创建一个统计生词频率的函数

def count_words(word, word_list):
    '''计算生词的中重复次数，返回该单词在列表中出现的次数'''
    count = 0
    for e in word_list:
        if e == word: 
            count += 1
    return count


# 将单词与其频率添加到键值对

for a in shengci_list:
    count = count_words(a, shengci_list)
    shengci_freq[a] = count

# 在命令行中显示出单词频率

# for k, v in shengci_freq.items():
#     print(k + " --- " + str(v) + "; ")

# print("\n")

# 挑选出频率大于三、等于二或一的单词

danci_freq_3a = [] # 频率大于等于3的生词列表
danci_freq_2 =[]  # 频率为2的生词列表
danci_freq_1 = [] # 频率为1的生词列表

for k, v in shengci_freq.items():
    if v >= 3:
        danci_freq_3a.append(k)
    elif v == 2:
        danci_freq_2.append(k)
    elif v == 1:
        danci_freq_1.append(k)

for i in danci_freq_3a:
    if len(i) <= 3:
        danci_freq_3a.remove(i)

for i in danci_freq_2:
    if len(i) <= 3:
        danci_freq_2.remove(i)

for i in danci_freq_1:
    if len(i) <= 3:
        danci_freq_1.remove(i)


# 过滤频率大于等于3的单词

unknown_temp_path = "C:\\Users\\bowen\\Desktop\\生词暂存备份.txt"
known_temp_path = "C:\\Users\\bowen\\Desktop\\熟词暂存备份.txt"

f3a_known_list = []
f3a_unknown_list = []

print("\n开始过滤频率>=3的单词：\n")
print("--------------------")

for i in sorted(danci_freq_3a):

    with open(known_temp_path, 'a') as kn_f_obj, \
        open(unknown_temp_path, 'a') as un_f_obj:

        #获取该单词位置
        position = str(danci_freq_3a.index(i)) + '/' + str(len(danci_freq_3a)) 

        print(position)

        answer = input("\n" + i + " 熟词按1，跳过按2，生词按3：\n")

        if answer == '1':
            f3a_known_list.append(i)
            kn_f_obj.write(i + " ") #写入暂存熟词
            print("\n------ " + i + " 已添加到熟词\n")
            
        elif answer == '3':
            f3a_unknown_list.append(i)
            un_f_obj.write(i + "***3+ \n") #写入暂存生词
            print("\n已添加到生词列表\n")
        else:
            print("\n已跳过\n")

# 过滤频率为2的单词

f2_known_list = []
f2_unknown_list = []

print("\n开始过滤频率为2的单词：\n")
print("--------------------")

for i in sorted(danci_freq_2):
    with open(known_temp_path, 'a') as kn_f_obj, \
        open(unknown_temp_path, 'a') as un_f_obj:

        #获取该单词位置
        position = str(danci_freq_2.index(i)) + '/' + str(len(danci_freq_2)) 
        print(position)

        answer = input("\n" + i + " 熟词按1，跳过按2，生词按3：\n")
        if answer == '1':
            f3a_known_list.append(i)
            kn_f_obj.write(i + " ") #写入暂存熟词
            print("\n------ " + i + " 已添加到熟词\n")
        elif answer == '3':
            f3a_unknown_list.append(i)
            un_f_obj.write(i + "***2 \n") #写入暂存生词
            print("\n已添加到生词列表\n")
        else:
            print("\n已跳过\n")


# 过滤频率为1的单词

f1_known_list = []
f1_unknown_list = []

print("\n开始过滤频率为1的单词：\n")
print("--------------------")

for i in sorted(danci_freq_1):
    with open(known_temp_path, 'a') as kn_f_obj, \
        open(unknown_temp_path, 'a') as un_f_obj:

        #获取该单词位置
        position = str(danci_freq_1.index(i)) + '/' + str(len(danci_freq_1)) 
        print(position)

        answer = input("\n" + i + " 熟词按1，跳过按2，生词按3：\n")
        if answer == '1':
            f3a_known_list.append(i)
            kn_f_obj.write(i + " ") #写入暂存熟词
            print("\n------ " + i + " 已添加到熟词\n")            
        elif answer == '3':
            f3a_unknown_list.append(i)
            un_f_obj.write(i + "***1 \n") #写入暂存生词
            print("\n已添加到生词列表\n")
        else:
            print("\n已跳过\n")

# 实际的生词率：

obj_for_statistic = clean_doc(obj_path, keep_all=True)
unknown_list = f1_unknown_list + f2_unknown_list + f3a_unknown_list

# 生词在文档中出现的总次数

count = 0
for a in unknown_list:
    i = count_words(a, obj_for_statistic)
    count += i

actural_percentage = str(round(count / len(obj_for_statistic) * 100, 1)) + "%"

count_msg1 = "\n本次单词总数：" + str(len(obj_for_statistic))
count_msg2 = "本次实际生词总数（含重复）：" + str(count)
count_msg3 = "本次实际生词率：" + actural_percentage 

count_msg = count_msg1 + "\n" + count_msg2 + "\n" + count_msg3

# 自定义导出文件名称

out_file_name = input("\n请输入导出文件的名称：")


'''
整理熟词
'''

# 把熟词写入到熟词库

known_list = f1_known_list + f2_known_list + f3a_known_list

with open("熟词库", 'a') as f_obj:

    # file_name = input("\n请输入本次文件名称：\n")

    a = "\n" #分割行，区分不同批次的熟词
    f_obj.write(a)
    lines = "------------------------------------------------------------------"
    count_info = "\n\n" + lines + "\n" + out_file_name + "\n" + count_msg1 + \
        "\n" + count_msg2 + "\n" + count_msg3 + "\n\n"

    f_obj.write(count_info) #写入统计信息

    for i in known_list:
        f_obj.write(i + ' ')

"""
导出
"""

# 导出三类频率的单词到txt

unknown_duizhao_path = "C:\\Users\\bowen\\Desktop\\" + out_file_name + \
    "生词频率参考.txt"

unknown_path = "C:\\Users\\bowen\\Desktop\\" + out_file_name + "生词.txt"

with open(unknown_duizhao_path, 'w') as f_obj:
    for k, v in shengci_freq.items():
        content = k + " --- " + str(v) + " \n"
        f_obj.write(content)

with open(unknown_path, 'w') as f_obj:
    count_info = count_msg1 + "\n" + count_msg2 + "\n" + count_msg3
    f_obj.write(count_info) #写入统计信息
    content = "\n\n以下是频率为1的生词：\n\n"
    f_obj.write(content)
    for i in f1_unknown_list:
        f_obj.write(i + ' ' + "\n")
    content = "\n以下是频率为2的生词：\n\n"
    f_obj.write(content)
    for i in f2_unknown_list:
        f_obj.write(i + ' ' + "\n")
    content = "\n以下是频率>=3的生词：\n\n"
    f_obj.write(content)
    for i in f3a_unknown_list:
        f_obj.write(i + ' ' + "\n")

# print(message)

print(count_info + "\n")
print("\n单词已分类保存\n")

# 保存