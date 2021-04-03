import re
import sys

with open("test2.txt", "r") as in_file:
    sys.stdout = open('out2.txt', 'w')

    names = []

    for line in in_file:
        striped_line = line.strip()
        res = re.findall(r'\w+', striped_line)
        curr_name = res[4]
        if curr_name in names:
            continue
        else:
            names.append(curr_name)
    names.sort()
    for name  in names:
        print(name)
    in_file.close()
    sys.stdout.close()
