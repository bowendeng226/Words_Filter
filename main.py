# 导入词库和要提取的文章，并转换成列表

from doctest import DONT_ACCEPT_BLANKLINE
from initializing_process import initializing_doc_main
import time
from pick_process import pick_main, count_words
from tools import get_running_time

# 用户输入方式获取生词位置

input_file_name = input("\n请输入生词文件名称（不要包含扩展名）：")
obj_path = "C:\\Users\\bowen\\Desktop\\" + input_file_name + ".txt"

# 获取初始化的文件

time_a = time.perf_counter()

user_prompt = "正在初始化文件......"
print(user_prompt)

basic_list = initializing_doc_main("familiar_vocabulary.txt")
basic_list = set(basic_list)
basic_list = list(basic_list)
basic_list = sorted(basic_list)
obj_list = initializing_doc_main(obj_path)

time_b = time.perf_counter()
running_time = get_running_time(time_a, time_b)
    
user_prompt = "文档初始化完成，单词数：" + str(len(obj_list)) + \
    "。用时：" + running_time + \
    "\n正在处理单词......"
print(user_prompt)

# 手动过滤进程

time_a = time.perf_counter()

word_count = pick_main(obj_list, basic_list)

# 统计熟词率，生词率

prompt = input("是否过滤长度小于6的单词(y/n)：")
if prompt.lower() == 'y':
    print("文档处理中......")
    for word in word_count[:]:
        if len(word) < 6:
            word_count.remove(word)
    # 过滤文档中的数字
    str_l = ""
    for word in word_count:
        str_l += (" " + str(word))
    numbers = list(range(0, 10))
    for n in numbers:
        if str(n) in str_l[:]:
            str_l.replace(str(n), '')
    word_count = str_l.split()

    
    shengci_count = 0
    for word in word_count:
        if word in obj_list:
            count = count_words(word, obj_list)
            shengci_count += count
else:
    shengci_count = 0
    for word in word_count:
        if word in obj_list:
            count = count_words(word, obj_list)
            shengci_count += count

time_b = time.perf_counter()

running_time = get_running_time(time_a, time_b)

print("过滤用时：" + running_time)

count_message = "生词数量（重复）：" + str(shengci_count) + "\n" + \
    "文档生词率：" + str(round(shengci_count / len(obj_list)*100, 2))+"%" + \
    "\n" +\
    "文档熟词率：" + \
    str(round((len(obj_list) - shengci_count) / len(obj_list) * 100, 2)) + "%"

print(count_message)


# def main(obj_path):

#     user_prompt = "正在初始化文件......"
#     print(user_prompt)

#     basic_list = initializing_doc_main("familiar_vocabulary.txt")
#     basic_list = set(basic_list)
#     basic_list = list(basic_list)
#     basic_list = sorted(basic_list)
#     obj_list = initializing_doc_main(obj_path)

#     time_b = time.perf_counter()
#     running_time = get_running_time(time_a, time_b)
        
#     user_prompt = "文档初始化完成，单词数：" + str(len(obj_list)) + \
#         "\n正在处理单词......"
#     print(user_prompt)

#     # 手动过滤进程

#     word_count = pick_main(obj_list, basic_list)

#     # 统计熟词率，生词率

#     shengci_count = 0
#     for word in word_count:
#         if word in obj_list:
#             count = count_words(word, obj_list)
#             shengci_count += count

#     count_message = "生词数量（重复）：" + str(shengci_count) + "\n" + \
#         "文档生词率：" + str(round(shengci_count / len(obj_list) * 100, 2))+"%"+\
#         "\n" + "文档熟词率：" + \
#         str(round((len(obj_list) - shengci_count) / len(obj_list) * 100, 2))+"%"

#     print(count_message)


