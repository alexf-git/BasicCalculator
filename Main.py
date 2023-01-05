from Calculation import Calculation


def welcome():
    print("------------A Simple Calculator - By: Alexandro Fernandez --------------")
    print("Possible Operations: +, -, *, /")
    print("To end calculator enter: '~'")
    print("------------------------------------------------------------------------")


def calculate():
    expression = input("Enter expression: ")

    if expression == '~':
        quit()

    calc = Calculation()
    calc.calculation(expression)


welcome()
calculate()
