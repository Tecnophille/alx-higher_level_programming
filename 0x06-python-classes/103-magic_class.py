#!/usr/bin/python3
"""magic class definition"""
import math


class MagicClass:
    """magicclass that makes same bytecode as in the task"""

    def __init__(self, radius=0):
        """Initialize class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """area function calculates some weird stuff"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """also this func calculate some weird stuff"""
        return (2 * math.pi) * self.__radius
