#!/usr/bin/python3
def safe_print_integer(value):
    value = int
    try:
        print("{:d}".format(value))
        if value is int:
            return (True)
    except(TypeError, ValueError):
        return (False)
