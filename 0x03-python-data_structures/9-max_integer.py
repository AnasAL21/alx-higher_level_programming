#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    big_num = my_list[0]
    for x in my_list:
        if x > big_num:
            big_num = x
            return big_num
