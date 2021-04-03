import re
import sys

with open('test3.txt', 'r') as in_file:
    sys.stdout = open('out3.txt', 'w')

    names = []
    counter = 0
    previous = ""

    for line in in_file:
        striped_line = line.strip()
        if (counter % 2) == 0:
            previous = striped_line
            counter += 1
            continue
        else:
            previous = previous + " " + striped_line
            print(previous)
            previous = ""
            counter += 1
            continue


    in_file.close()
    sys.stdout.close()
