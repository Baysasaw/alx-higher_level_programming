#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
            """
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    @property
    def width(self):
        return self.__width
    def height(self):
        return self.__height
    def x(self):
        return self.__x
    def y(self):
        return self.__y