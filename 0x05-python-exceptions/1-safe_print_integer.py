#!/usr/bin/python3
def safe_print_integer(value):
    value = int
    print("{:d}".format(value))
    try:
        if value is int:
            return True
    except:
        return False
