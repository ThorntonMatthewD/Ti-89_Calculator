import re


class BaseMode:
    def __init__(self):
        super()

    # Every class that inherits from this one will be able to meow.
    def meow(self):
        print("Meow!!")
