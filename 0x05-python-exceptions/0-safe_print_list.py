#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0:
        for i in range(len(my_list)):
            try:
                print(my_list[i])
                count = i + 1
                if count == x:
                    break
            except:
                pass
            print()
            return (count)
