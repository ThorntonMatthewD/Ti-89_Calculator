import sympy as sym

from modes.base_mode import BaseMode


class DerivMode(BaseMode):
    # A blank constructor for this class
    def __init__(self):
        super().__init__()

    def calculate(self, expression):
        return eval(f"sym.{expression}")
