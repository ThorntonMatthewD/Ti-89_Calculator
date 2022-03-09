import cmath as cm

from modes.base_mode import BaseMode


class ComplexMode(BaseMode):
    # A blank constructor for this class
    def __init__(self):
        super().__init__()

    def calculate(self, expression):
        return eval(f"cm.{expression}")
