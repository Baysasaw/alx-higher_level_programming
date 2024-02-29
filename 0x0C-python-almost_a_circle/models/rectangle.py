from models.base import Base


"""Defines a rectangle model class"""
class Rectangle(Base):
    """
    Rectangle model
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