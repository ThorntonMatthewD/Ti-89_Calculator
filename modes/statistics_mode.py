from modes.base_mode import BaseMode
import statistics as s


class StatsMode(BaseMode):
    def __init__(self):
        super().__init__()

    def calculate(self, expression):
        return eval(f"s.{expression}")

    def meow(self):
        print(
            "I don't want to meow like the others. I'm going to override the meow method I inherited from my parent class."
        )
