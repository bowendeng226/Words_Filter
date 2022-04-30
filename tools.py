"""本文件中储存的是与主程序无关的，但却被用到的一些工具，例如计时器等
本文件包含：计时器
"""
import os
# from main import main

def get_running_time(time_1, time_2):
    """计算运行时间，返回字符串，e.g.“20sec"、"20min20sec"

    Args:
        time_1 (_type_): 锚点时间一
        time_2 (_type_): 锚点时间二

    Returns:
        _type_: _description_
    """
    middle_time = time_2 - time_1
    if middle_time >= 60:
        minites = int(middle_time / 60)
        seconds = round(middle_time % 60)
        run_time = str(minites) + "min" + str(seconds) + "sec"
        return run_time
    else:
        run_time = str(round(middle_time, 2)) + "sec"
        return run_time


# def little_docs(doc_file):
#     """

#     Args:
#         doc_list (_type_): _description_
#     """
#     doc_list = os.listdir(doc_file)
#     for doc in doc_list:
        