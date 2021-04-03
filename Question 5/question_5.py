import re
import sys

with open("test4_Fixlog.log", "r") as in_file:
    sys.stdout = open('out5.txt', 'w')

    storage = []
    log_date = ""

    for line in in_file:
        striped_line = line.strip()
        
        line = striped_line.split(" ")
        log_date = line[0]
        line = line[1].split("|")

        for elem in line:
            tag = elem.split("=")
            if tag[0] == "52":
                curr_code = tag[1]

                if curr_code in storage:
                    break
                else:
                    print(log_date + " " + curr_code)
                    storage.append(curr_code)
                    break
            else:
                continue
    

    in_file.close()
    sys.stdout.close() 
