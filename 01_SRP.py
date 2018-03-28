"""
1 High-level modules should not depend on low-level modules. Both should depend on abstractions.
2 Abstractions should not depend on details. Details should depend on abstractions.
"""


class ElectricOven(object):

    def __init__(self):
        self.Name = "electrict Oven"


class Kitchen(object):

    def __init__(self):
        self.oven = ElectricOven()