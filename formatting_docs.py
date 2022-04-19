


# file_name = "C:\\Users\\bowen\\desktop\\L3_unformated.txt"


def formatting_doc(file_name):
    """
    去除txt文档里的去除txt文档里的多余空格、换行符、制表符等；
    将文档里的单词全部小写
    去除文档里的单字母
    去除数字 （未开发...）
    返回一个列表

    Args:
        file_name (_txt_): _接收一个txt文档_

    Returns:
        _list_: _返回包含该txt文档所有符合条件单词的列表_
    """

    # 全角和半角标点符号 以及数字

    half_punctuations = "`~!@#$%^&*()-_=+[{]}\|;:'" + '",<.>/?'
    full_punctuations = "·~！@#￥%……&*（）-——=+【{】}、|；：‘’“”，《。》/？"
    numbers = "0123456789"
    punctuations = half_punctuations + full_punctuations + numbers

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

    # 去除列表中的空格和长度小于3的元素

    for i in list_clean[:]:
        if i == ' ' or len(i) < 4:
            list_clean.remove(i)

    return list_clean

# list_clean = clean_doc(file_name)

# save_file = "C:\\Users\\bowen\\desktop\\L3_formatted.txt"

# with open(save_file, 'w') as f_obj:
#     for i in list_clean:
#         f_obj.write(i + ' ')


