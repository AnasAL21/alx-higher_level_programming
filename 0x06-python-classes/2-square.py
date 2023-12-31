#!/usr/bin/python3
"""Def a class Square."""


class Square:
    """Representing square."""

    def __init__(self, size=0):
        """Initializing new Square.

        Args:
            size (int): size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
