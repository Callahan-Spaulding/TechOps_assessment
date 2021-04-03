import re
import sys

with open("gelber_ops.log", "r") as in_file:
    sys.stdout = open('out7.txt', 'w')

    

    for line in in_file:
        striped_line = line.strip()
        if '[warn]' in striped_line.lower():
            print striped_line
        elif '[error]' in striped_line.lower():
            print striped_line
        elif '[fatal]' in striped_line.lower():
            print striped_line
        



    sys.stdout.close()
    in_file.close()
