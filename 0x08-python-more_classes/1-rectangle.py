#!/usr/bin/python3
# 0-rectangle.py
"""Defines a Rectangle class."""

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
        return self.width
    
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
    def height(self):
        return self.height
    
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
