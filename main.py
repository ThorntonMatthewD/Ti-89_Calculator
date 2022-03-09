# from modes.derivative_mode import DerivMode
from modes.complex_mode import ComplexMode
from modes.real_mode import RealMode
from modes.statistics_mode import StatsMode


if __name__ == "__main__":
    expression = ""
    # expression = input("Type your math equation -> ")
    run = True

    # MODES = [RealMode(), ComplexMode(), DerivMode(), StatsMode()]
    MODES = [RealMode("A parameter for a mode class!"), ComplexMode(), StatsMode()]
    current_mode_idx = 0

    # Accessing the parameter inside of RealMode
    MODES[0].get_some_val()

    while run:
        # calculatorBtn =
        mode_selection = input("Which calculator mode would you like to use? ")

        match mode_selection.lower():
            case "real":
                print("You have selected real mode!")
                current_mode_idx = 0
            case "complex":
                print("You have selected complex mode!")
                current_mode_idx = 1
            # case "derivative":
            #   print("You have selected derivative mode!")
            #  current_mode_idx = 2
            case "statistics":
                print("You have selected statistics mode!")
                current_mode_idx = 2
            case _:
                print("You didn't make a valid selection. Try again!")
                current_mode_idx = 0

        MODES[current_mode_idx].meow()
