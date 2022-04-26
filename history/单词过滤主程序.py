# 导入词库和要提取的文章，并转换成列表

from doctest import DONT_ACCEPT_BLANKLINE


# 导入

basic_library_path = "C:\\Users\\bowen\\OneDrive\\Code\\单词过滤系统\\熟词库.txt"
input_file_name = input("\n请输入要导入的文件名称（不要包含扩展名）：")
obj_path = "C:\\Users\\bowen\\Desktop\\" + input_file_name + ".txt"

with open(basic_library_path) as f_obj:
    contents = f_obj.read()
    basic = contents.split()

with open(obj_path) as f_obj:
    contents = f_obj.read()
    w_obj = contents.split()

# 格式化：将要过滤的列表和熟词列表全部小写并排序

fo_basic = []
for word in basic:
    fo_basic.append(word.lower())
fo_basic = sorted(fo_basic)

fo_obj = []
for word in w_obj:
    fo_obj.append(word.lower())
fo_obj = sorted(fo_obj)

copy_obj = fo_obj[:] # 复制最初的生词列表，以备统计生词率

# 过滤

shengci = []
shuci = []
for word in fo_obj:
    if word in fo_basic:
        shuci.append(word.lower())
    else:
        shengci.append(word.lower())

# 过滤生词和熟词中长度小于3的单词

for word in shengci:
    if len(word) < 4:
        shengci.remove(word)

for word in shuci:
    if len(word) < 4:
        shuci.remove(word)

# 展示

message = "\n总计单词（含重复）：" + str(len(fo_obj)) + "\n" + \
    "生词（含重复）：" + str(len(shengci)) + "\n" + \
    "此处统计（含重复）的生词/全词比：" + \
    str(round(len(shengci)/len(fo_obj)*100, 1)) + "%" + "\n"

# 剔除熟词重复项

shuci = set(shuci)
shuci = list(shuci)


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

for a in shengci:
    count = count_words(a, shengci)
    shengci_freq[a] = count

# 在命令行中显示出单词频率

for k, v in shengci_freq.items():
    print(k + " --- " + str(v) + "; ")

print("\n")

# 挑选出频率大于三、等于二或一的单词

danci_freq_3a = []
danci_freq_2 =[]
danci_freq_1 = []
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

for li in [danci_freq_1, danci_freq_2, danci_freq_3a]:
    print(li)
    print("\n")

# 从上次的位置恢复

get_recover = input("\n是否从上次的位置恢复？y/n\n")

if get_recover.lower() == 'y':
    get_list_name = input("\n请选择上次位置：3频率>=3；2频率=2；1频率=1\n")
    position_prompt = "\n请输入上次位置的索引值或单词：\n"
    get_position = input(position_prompt)
    if len(get_position) <= 3:
        input_type = True
    if len(get_position) > 3:
        input_type = False
        
    if input_type and get_list_name == '3':
        danci_freq_3a = danci_freq_3a[int(get_position):] #仅保留索引值后的内容
    if input_type and get_list_name == '2':
        danci_freq_3a = [] #删除频率3列表内容
        danci_freq_2 = danci_freq_2[int(get_position):]
    if input_type and get_list_name == '1':
        danci_freq_3a = []
        danci_freq_2 = []
        danci_freq_1 = danci_freq_1[int(get_position):]

    if input_type == False:
        if get_list_name == '3':
            numb = danci_freq_3a.index(get_position)
            danci_freq_3a = danci_freq_3a[numb:]
        if get_list_name == '2':
            numb = danci_freq_2.index(get_position)
            danci_freq_3a = []
            danci_freq_2 = danci_freq_2[numb:]
        if get_list_name == '1':
            numb = danci_freq_1.index(get_position)
            danci_freq_3a = []
            danci_freq_2 = []
            danci_freq_1 = danci_freq_1[numb:]
        




# 主动式在生词列表中挑选出熟词

# 为避免很长的项目中途退出不能保存单词，因此开发暂存机制

# 过滤频率大于等于3的单词

unknown_temp_path = "C:\\Users\\bowen\\Desktop\\生词暂存备份.txt"
known_temp_path = "C:\\Users\\bowen\\Desktop\\熟词暂存备份.txt"


# 尝试
# count_list = len(danci_freq_1)

# active = True
# while active:
#     with open(unknown_temp_path, 'a') as un_fobj, \
#         open(known_temp_path, 'a') as kn_fobj:

# f1_known_list = []
# f1_unknown_list = []

# for i in danci_freq_1:
#     with open(unknown_temp_path, 'a') as un_fobj, \
#         open(known_temp_path, 'a') as kn_fobj:
#         answer = input("...")
#         if answer == '1':
#             f1_known_list.append(i + " ")
#             kn_fobj.write(i + ' ')
#         elif answer == '3':
#             f1_unknown_list.append(i + " ")
#             un_fobj.write(i + "***1 ")



# 尝试

# with open(unknown_temp_path, 'a') as un_fobj, \
#     open(known_temp_path, 'a') as kn_fobj:

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


# f2_known_list = []
# f2_unknown_list = []

# print("\n开始过滤频率为2的单词：\n")
# print("--------------------")

# for i in danci_freq_2:

#     answer = input(i + " 熟词按1，跳过按2，生词按3：")

#     if answer == '1':
#         f2_known_list.append(i)
#         kn_fobj.write(i + " ") #写入暂存熟词
#         print("------" + i + " 已添加到熟词\n" + str(len(f2_known_list)) + \
#             '/' + str(len(danci_freq_2)) + "\n")
#     elif answer == '3':
#         f2_unknown_list.append(i)
#         un_fobj.write(i + "***2 \n") #写入暂存生词
#         print("已添加到生词列表\n")

#     else:
#         print("已跳过\n")


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


# f1_known_list = []

# f1_unknown_list = []

# print("\n开始过滤频率为1的单词：\n")

# print("--------------------")

# for i in danci_freq_1:

#     answer = input(i + " 按1添加到熟词：")

#     if answer == '1':
#         f1_known_list.append(i)
#         kn_fobj.write(i + " ") #写入暂存熟词
#         print("------" + i + " 已添加到熟词\n" + str(len(f1_known_list)) + \
#             '/' + str(len(danci_freq_1)) + "\n")
#     elif answer == '3':
#         f1_unknown_list.append(i)
#         un_fobj.write(i + "***1 \n") #写入暂存生词
#         print("已添加到生词列表\n")
#     else:
#         print("已跳过\n")


# 实际的生词率：

unknown_list = f1_unknown_list + f2_unknown_list + f3a_unknown_list

count = 0

for a in unknown_list:
    i = count_words(a, copy_obj)
    count += i

actural_percentage = str(round(count / len(copy_obj) * 100, 1)) + "%"

count_msg1 = "\n本次单词总数：" + str(len(copy_obj))

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

with open(basic_library_path, 'a') as f_obj:

    # file_name = input("\n请输入本次文件名称：\n")

    a = "\n" #分割行，区分不同批次的熟词

    f_obj.write(a)

    lines = "------------------------------------------------------------------"

    count_info = "\n\n" + lines + "\n" + out_file_name + "\n" + count_msg1 + \
        "\n" + count_msg2 + "\n" + count_msg3 + "\n\n"

    f_obj.write(count_info) #写入统计信息

    for i in known_list:
        f_obj.write(i + ' ')


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

print(message)

print(count_msg + "\n")

print("\n单词已分类保存\n")

# 保存