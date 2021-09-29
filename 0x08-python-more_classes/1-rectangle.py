#!/usr/bin/python3
"""Class/module Rectangle"""


class Rectangle:
    """Object Rectangle"""
    dict

    def __init__(self, width=0, height=0):
        """Constructor"""
        if type(width) is not int or type(height) is not int:
            raise TypeError("{} must be an integer".format(
                "width" if type(width) is not int else "height"))
        if width < 0 or height < 0:
            raise ValueError("{} must be >= 0".format(
                "width" if width < 0 else "height"))
        self.__height = height
        self.__width = width

    """Get width"""
    def get_width(self):
        return self.__width

    """Set width"""
    def set_width(self, value):
        return self.__init__(value, self.__height)

    """Get height"""
    def get_height(self):
        return self.__height

    """Set height"""
    def set_height(self, value):
        return self.__init__(self.__width, value)

    width = property(get_width, set_width)
    height = property(get_height, set_height)