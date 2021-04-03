import re
import sys

with open("test4_Fixlog.log", "r") as in_file:
    sys.stdout = open('out4.txt', 'w')

    storage = []


    for line in in_file:
        striped_line = line.strip()
        line = striped_line.split("|")
        for elem in line:
            tag = elem.split("=")
            if tag[0] == "52":
                curr_code = tag[1]
            
                if curr_code in storage:
                    break
                else:
                    print curr_code
                    storage.append(curr_code)
                    break
            else:
                continue


    in_file.close()
    sys.stdout.close()
