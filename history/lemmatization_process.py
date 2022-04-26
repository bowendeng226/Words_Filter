from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag

# 将文档转换为列表

from clean_docs import clean_doc

words_list = clean_doc('熟词库.txt')
comparison_list = clean_doc('熟词库.txt')

# 获取单词的词性
def get_wordnet_pos(tag):
    """
    传入单词-词性的元组列表，返回词性
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

# parts = pos_tag(words_list) # pos_tag获取单词列表，返回[(单词, 词性)]的元组列表

# wnl = WordNetLemmatizer()

# lemmas_sent = []
# for part in parts:
#     wordnet_pos = get_wordnet_pos(part[1]) or wordnet.NOUN
#     lemmas_sent.append(wnl.lemmatize(part[0], pos = wordnet_pos)) # 词性还原

def lemmatization_process(words_list):
    """传入要词形还原的单词列表，返回还原后的单词列表

    Args:
        words_list (_type_): _description_
    """
    parts = pos_tag(words_list) # pos_tag获取单词列表，返回[(单词, 词性)]的元组列表
    wnl = WordNetLemmatizer()

    lemmas_sent = []
    for part in parts:
        wordnet_pos = get_wordnet_pos(part[1]) or wordnet.NOUN
        lemmas_sent.append(wnl.lemmatize(part[0], pos = wordnet_pos)) # 词性还原

    return lemmas_sent

# print(lemmas_sent)

# sentence = 'ate, loves, learned'
# tokens = word_tokenize(sentence)  # 分词
# tagged_sent = pos_tag(tokens)     # 获取单词词性

# wnl = WordNetLemmatizer()
# lemmas_sent = []
# for tag in tagged_sent:
#     wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
#     lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos)) # 词形还原

# print(lemmas_sent)


# comparison_dic = {}
# i = 0
# while i < (len(comparison_list) - 1):
#     comparison_dic[words_list[i]] = lemmas_sent[i]
#     i += 1

# for k, v in comparison_dic.items():
#     print(k + ": " + v)


# i = 0
# filtered = []
# while i < len(comparison_list) - 1:
#     if comparison_list[i] != lemmas_sent[i]:
#         filtered.append(comparison_list[i] + ": " + lemmas_sent[i])
#     i += 1

# print("Total: " + str(len(comparison_list)))
# print(len(filtered))
# for a in filtered:
#     print(a)
