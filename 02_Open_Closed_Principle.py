""" class should be open for extension but closed for modification. """
import math


class Shape(object):

    def __init__(self, shape_type, **kwarks):
        self.shape_type = shape_type
        for key in kwarks:
            setattr(self,key,kwarks[key])

    def calculate_area(self):
        if self.shape_type == "SQUARE":
            return self.a ** 2
        if self.shape_type == "CIRCLE":
            return math.pi * self.r ** 2
        if self.shape_type == "RECTANGLE":
            return self.a * self.b


#####
"""
    FizzBuzz Problem
    print any number divisible by three with the word “fizz” instead of the number.
    print any number divisible by five with the word “buzz” instead of the number.
    print any number divisible by seven with the word “bang” instead of the number.
"""
x = 105

if x%7 == 0 and x%3 == 0 and x%5 == 0:
	print("FizzBuzzBang")
elif x%7 == 0 and x%5 == 0:
	print("BuzzBang")
elif x%7 == 0 and x%3 == 0:
	print("FizzBang")
elif x%3 == 0 and x%5 == 0:
	print("FizzBuzz")
elif x%7 == 0:
	print("Bang")
elif x%5 == 0:
	print("Buzz")
elif x%3 == 0:
	print("Fizz")
else:
	print(x)


















class FizzBuzzFactory(object):
    def create(self):
        rules = [FizzBuzzBangRule(), BuzzBangRule(), FizzBangRule(), FizzBuzzRule(),
                 BangRule(), BuzzRule(), FizzRule(), NormalRule()]
        return FizzBuzz(rules)


class FizzBuzz(object):

    def __init__(self, rules):
        self.rules = rules

    def say(self, x):
        for rule in self.rules:
            if rule.is_handle(x):
                return rule.say(x)


class Rule(object):
    def is_handle(self, x):
        pass

    def say(self, x):
        pass


class NormalRule(Rule):
    def is_handle(self, x):
        return True

    def say(self, x):
        return x


class FizzRule(Rule):
    def is_handle(self, x):
        return x % 3 == 0

    def say(self, x):
        return "Fizz"


class BuzzRule(Rule):
    def is_handle(self, x):
        return x % 5 == 0

    def say(self, x):
        return "Buzz"


class BangRule(Rule):
    def is_handle(self, x):
        return x % 7 == 0

    def say(self, x):
        return "Bang"


class FizzBuzzRule(Rule):
    def is_handle(self, x):
        return x % 5 == 0 and x % 3 == 0

    def say(self, x):
        return "FizzBuzz"


class FizzBangRule(Rule):
    def is_handle(self, x):
        return x % 7 == 0 and x % 3 == 0

    def say(self, x):
        return "FizzBang"


class BuzzBangRule(Rule):
    def is_handle(self, x):
        return x % 7 == 0 and x % 5 == 0

    def say(self, x):
        return "BuzzBang"


class FizzBuzzBangRule(Rule):
    def is_handle(self, x):
        return x % 7 == 0 and x % 5 == 0 and x % 3 == 0

    def say(self, x):
        return "FizzBuzzBang"


if __name__ == '__main__':
    l = [1, 2, 3, 6, 5, 15, 20]
    fizz_buzz = FizzBuzzFactory().create()
    for x in l:
        print(fizz_buzz.say(x))