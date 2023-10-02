#!/usr/bin/python3
"""Define a Rectangle"""

class Rectangle:
    """represent a Rectangle"""
    def __init__(self, width = 0, lenght = 0):
        """initialize a rectangle.
        
        Args:
            width (int): the measure of how wide an object is.
            lenght (int): the measure of how long an object is. 
        """
        self.width = w
        self.lenght = l
        
    @property
    def width(self):
        return self.width
    
    @width.setter
    def width(self, w):
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        elif w < 0:
            raise ValueError("width must be >= 0")
        
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, l):
        if not isinstance(l, int):
            raise TabError("height must be an intger")
        elif l < 0:
            raise ValueError("height must be >= 0")
