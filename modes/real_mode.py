import math as m

from modes.base_mode import BaseMode


class RealMode(BaseMode):
    # This constructor takes in a parameter and sets it to a class attribute
    def __init__(self, some_val):
        super().__init__()

        self.some_val = some_val

    def calculate(self, expression):
        return eval(f"m.{expression}")

    def get_some_val(self):
        print(f"some_val = {self.some_val}")
        return self.some_val
