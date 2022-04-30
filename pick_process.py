
def pick_words(object_list, basic_list):
    """传入要过滤的单词列表，以及熟词库列表，将要过滤的列表中的生词捡出来，返回包含
    生词和熟词的元组或列表
    """
    shengci_list = []
    shuci_list = []

    for word in object_list:
        if word in basic_list:
            shuci_list.append(word.lower())
        else:
            shengci_list.append(word.lower())
    
    return [shengci_list, shuci_list]


def count_words(word, word_list):
    """传入一个单词和一个由单词组成的列表，计算该单词在列表中出现的次数，返回整数int

    Args:
        word (_type_): _description_
        word_list (_type_): _description_
    """
    count = 0
    for w in word_list:
        if w == word: 
            count += 1
    return count


def get_word_frequency(word_list):
    """传入生词的列表，返回不同词频的单词列表

    Args:
        word (_type_): _description_
        word_list (_type_): _description_
    """
    word_freq = {}
    for a in word_list:
        count = count_words(a, word_list)
    word_freq[a] = count

    danci_freq_3a = [] # 频率大于等于3的生词列表
    danci_freq_2 =[]  # 频率为2的生词列表
    danci_freq_1 = [] # 频率为1的生词列表

    for k, v in word_freq.items():
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

    return [danci_freq_1, danci_freq_2, danci_freq_3a]


def final_pick(word_list):
    """_summary_

    Args:
        word_list (_type_): _description_
    """
    # unknown_temp_path = "C:\\Users\\bowen\\Desktop\\生词暂存备份.txt"
    # known_temp_path = "C:\\Users\\bowen\\Desktop\\熟词暂存备份.txt"
    known_words = []
    unknown_words = []
    # user_prompt = "====================\n开始过滤词频>=3的单词......" 
    # print("\n开始过滤频率>=3的单词：\n")
    # print("====================")
    for i in sorted(word_list):
        #获取该单词位置
        position = str(word_list.index(i)) + '/' + str(len(word_list)) 
        print(position) # 提示完成度

        answer = input(i + " 熟词按1，跳过按2，生词按3：")
        if answer == '1':
            known_words.append(i)
            # kn_f_obj.write(i + " ") #写入暂存熟词
            print("------ " + i + " 已添加到熟词\n")
        elif answer == '3':
            unknown_words.append(i)
            # un_f_obj.write(i + "***3+ \n") #写入暂存生词
            print("已添加到生词列表\n")
        else:
            print("已跳过\n")
    return [known_words, unknown_words]


def pick_main(object_list, basic_list):
    """
    返回不包含重复的单词统计信息
    """
    # 提取生词列表
    word_list = pick_words(object_list, basic_list)
    shengci_list = word_list[0]
    shuci_list = word_list[1]
    kn_i = len(shuci_list)

    # 获取词频列表
    freq_list = get_word_frequency(shengci_list)
    freq_1 = freq_list[0]
    freq_2 = freq_list[1]
    freq_3a = freq_list[2]

    print("本次需要过滤的单词数量：" + str(len(freq_1 + freq_2 + freq_3a)))

    unknown_f_name = r"C:\users\bowen\desktop\本次生词.txt"
    known_f_name = r"C:\users\bowen\desktop\本次熟词"

    # 过滤词频大于等于3的单词
    print("Frequency 3 words start: \n")
    picked_words = final_pick(freq_3a)
    known_words = picked_words[0]
    unknown_words = picked_words[1]
    with open(unknown_f_name, 'a') as un_obj, \
        open(known_f_name, 'a') as kn_obj:
        un_obj.write("Words frequency >= 3: \n")
        for w in unknown_words:
            un_obj.write(w + " ")
        for w in known_words:
            kn_obj.write(w + " ")
    un_i = len(unknown_words) # 计算单词数
    kn_i += len(known_words)
    word_count = [unknown_words]

    # 词频2
    print("Frequency 2 words start: \n")
    picked_words = final_pick(freq_2)
    known_words = picked_words[0]
    unknown_words = picked_words[1]
    with open(unknown_f_name, 'a') as un_obj, \
        open(known_f_name, 'a') as kn_obj:
        un_obj.write("Words frequency 2: \n")
        for w in unknown_words:
            un_obj.write(w + " ")
        for w in known_words:
            kn_obj.write(w + " ")
    un_i += len(unknown_words)
    kn_i += len(known_words)
    word_count += unknown_words

    # 词频1
    print("Frequency 1 words start: \n")
    picked_words = final_pick(freq_1)
    known_words = picked_words[0]
    unknown_words = picked_words[1]
    with open(unknown_f_name, 'a') as un_obj, \
        open(known_f_name, 'a') as kn_obj:
        un_obj.write("Words frequency 1: \n")
        for w in unknown_words:
            un_obj.write(w + " ")
        for w in known_words:
            kn_obj.write(w + " ")
    un_i += len(unknown_words)
    kn_i += len(known_words)
    word_count += unknown_words
    # return [un_i, kn_i]
    return word_count


    


    





