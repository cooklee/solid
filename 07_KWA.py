"""
Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it.
"""


class Bird(object):
    def __init__(self):
        pass

    def fly(self):
        # do something
        pass


class Pinguin(Bird):
    def __init__(self):
        pass

    def fly(self):
        raise Exception("i cant fly")



#####

class Rectangle(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_widht(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height



class Squere(Rectangle):

    def __init__(self, side):
        self.side = side

    #???




