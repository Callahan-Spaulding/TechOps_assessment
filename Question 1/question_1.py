import re
import sys

with open("test.txt", "r") as in_file:
    sys.stdout = open('out.txt', 'w')
    for line in in_file:
        striped_line = line.strip()
        res = re.findall(r'\w+', striped_line)
        print(res[4])
    in_file.close()
    sys.stdout.close()
