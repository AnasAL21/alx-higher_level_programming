#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0:
    for i in range(len(my_list)):
        try:
            print(my_list[i], end="")
            count = count + 1
        except:
            break
    print("")
    return (count)
