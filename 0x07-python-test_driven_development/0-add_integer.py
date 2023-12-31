#!/usr/bin/python3
def add_integer(a, b=98):
    """Returns an integer: the addition of a and b.
       a and b must be integers or floats."""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
