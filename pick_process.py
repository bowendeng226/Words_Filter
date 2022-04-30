
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
    known_words = []
    unknown_words = []

    for i in sorted(word_list):

        #获取该单词位置
        position = str(word_list.index(i) + 1) + '/' + str(len(word_list)) 
        print(position) # 提示完成度

        answer = input(i + " 熟词按1，跳过按2，生词按3：")
        if answer == '1':
            known_words.append(i)
            # kn_f_obj.write(i + " ") #写入暂存熟词
            print("------ " + i + " 已添加到熟词\n")
        elif answer == '3':
            unknown_words.append(i)
            print("已添加到生词列表\n")
        else:
            print("已跳过\n")
    return [known_words, unknown_words]


def pick_main(object_list, basic_list):
    """
    """
    # 提取生词列表
    word_list = pick_words(object_list, basic_list)
    shengci_list = word_list[0]
    shuci_list = word_list[1]

    # 获取词频列表
    freq_list = get_word_frequency(shengci_list)
    freq_1 = freq_list[0]
    freq_2 = freq_list[1]
    freq_3a = freq_list[2]

    unknown_f_name = r"C:\users\bowen\desktop\本次生词.txt"
    known_f_name = r"C:\users\bowen\desktop\本次熟词"

    prompt = input("是否需要精确过滤(y/n)：")

    if prompt.lower() == 'y':
        print("开始手动过滤......")
        print("本次需要过滤的单词数量：" + str(len(freq_1 + freq_2 + freq_3a)))

        # 过滤词频大于等于3的单词
        print("Frequency 3 words start: \n")
        picked_words = final_pick(freq_3a)
        known_words = picked_words[0]
        unknown_words = picked_words[1]
        with open(unknown_f_name, 'a') as un_obj, \
            open(known_f_name, 'a') as kn_obj:
            un_obj.write("\nWords frequency >= 3: \n")
            for w in unknown_words:
                un_obj.write(w + " ")
            for w in known_words:
                kn_obj.write(w + " ")

        word_count = [unknown_words]

        # 词频2
        print("Frequency 2 words start: \n")
        picked_words = final_pick(freq_2)
        known_words = picked_words[0]
        unknown_words = picked_words[1]
        with open(unknown_f_name, 'a') as un_obj, \
            open(known_f_name, 'a') as kn_obj:
            un_obj.write("\n\nWords frequency 2: \n")
            for w in unknown_words:
                un_obj.write(w + " ")
            for w in known_words:
                kn_obj.write(w + " ")

        word_count += unknown_words

        # 词频1
        print("Frequency 1 words start: \n")
        picked_words = final_pick(freq_1)
        known_words = picked_words[0]
        unknown_words = picked_words[1]
        with open(unknown_f_name, 'a') as un_obj, \
            open(known_f_name, 'a') as kn_obj:
            un_obj.write("\n\nWords frequency 1: \n")
            for w in unknown_words:
                un_obj.write(w + " ")
            for w in known_words:
                kn_obj.write(w + " ")

        word_count += unknown_words
        return word_count
    else:
        with open(unknown_f_name, 'a') as unknown_obj, \
            open(known_f_name, 'a') as known_obj:
            unknown_obj.write("\nWords frequency 3a: \n")
            for word in freq_3a:
                unknown_obj.write(word + " ")
            unknown_obj.write("\n\nWords frequency 2: \n")
            for word in freq_2:
                unknown_obj.write(word + " ")
            unknown_obj.write("\n\nWords frequency 1: \n")
            for word in freq_1:
                unknown_obj.write(word + " ")
            
            word_count = freq_1 + freq_2 + freq_3a
            return word_count

    


    





