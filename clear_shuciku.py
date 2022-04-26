from initializing_process import initializing_doc_main
import time

time_1 = time.perf_counter()

formatted_file = initializing_doc_main("熟词库.txt")
for_statistic_before = len(formatted_file)

with open("familiar_vocabulary.txt", 'a') as fobj:
    formatted_file = set(formatted_file)
    formatted_file = list(formatted_file)
    formatted_file = sorted(formatted_file)
    for_statistic_after = len(formatted_file)
    for a in formatted_file:
        fobj.write(a + " ")

    info = "Before: " + str(for_statistic_before) + "\n" + "After: " + \
        str(for_statistic_after)
    fobj.write("\nBefore: " + str(for_statistic_before) + "\n" + "After: " + \
        str(for_statistic_after))

time_2 = time.perf_counter()

duration = round(time_2 - time_1, 2)

print(info)

print("Duration: " + str(duration) + "seconds")

    
