from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag

def clean_doc(file_name, keep_all=True):
    """
    去除txt文档里的去除txt文档里的多余空格、换行符、制表符等；
    将文档里的单词全部小写
    去除文档里的单字母
    去除数字 （未开发...）
    对单词进行排序
    返回一个列表

    Args:
        file_name (_txt_): _接收一个txt文档_

    Returns:
        _list_: _返回包含该txt文档所有符合条件单词的列表_
    """

    # 全角和半角标点符号
    half_punctuations = "`~!@#$%^&*()-_=+[{]}\|;:'" + '",<.>/?'
    full_punctuations = "·~！@#￥%……&*（）-——=+【{】}、|；：‘’“”，《。》/？"
    punctuations = half_punctuations + full_punctuations

    # 去除文档里的标点符号
    with open(file_name) as f_obj:
        contents = f_obj.read()
        for p in punctuations:
            if p in contents:
                contents = contents.replace(p, ' ')

    # 将单词转为列表
    content_list = contents.split()

    # 去除元素的前后空格以及全部小写
    list_clean = []
    for i in content_list:
        i = i.strip().lower()
        list_clean.append(i)

    if keep_all: # 如果要求保留完整的单词列表
        for i in list_clean[:]:
            if i == " " or "":
                list_clean.remove(i)
    elif keep_all == False: # 如果不保留完整列表
        # 去除列表中的空格和长度小于等于3的元素
        for i in list_clean[:]:
            if i == ' ' or len(i) < 4:
                list_clean.remove(i)

    # 对列表排序
    list_clean = sorted(list_clean)

    return list_clean


def get_wordnet_pos(tag):
    """
    传入单词-词性的元组列表，返回单词词性
    """
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def initializing_doc_main(file):
    """传入要词形还原的文档，返回还原后的单词列表

    Args:
        words_list (_type_): _description_
    """
    words_list = clean_doc(file) # 获取干净的单词列表
    parts = pos_tag(words_list) # pos_tag获取单词列表，返回[(单词, 词性)]的元组列表
    wnl = WordNetLemmatizer()

    lemmas_sent = []
    for part in parts:
        wordnet_pos = get_wordnet_pos(part[1]) or wordnet.NOUN
        lemmas_sent.append(wnl.lemmatize(part[0], pos = wordnet_pos)) # 词性还原

    return lemmas_sent


