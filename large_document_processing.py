"""处理大型文档的一些方便工具"""

file_name = r"C:\users\bowen\desktop\SRLJJSJXT.txt"

with open(file_name) as f_obj:
    contents = f_obj.read()
    chapters = contents.split("@thisistitle@")

dir_path = r"C:\users\bowen\desktop\CSAPP-"

i = 1
for chapter in chapters:
    with open(dir_path + str(i) + ".txt", 'w') as f_obj:
        for word in chapter:
            f_obj.write(word)
    i += 1
