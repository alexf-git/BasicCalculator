from Operations import Operations
from Calculation import Calculation

def welcome():
    print("------------A Simple Calculator - By: Alexandro Fernandez --------------")
    print("Possible Operations: +, -, *, /")
    print("To end calculator enter: '~'")
    print("------------------------------------------------------------------------")
    pass

def calculate():
    expression = input("Enter expression: ")

    if expression == '~':
        quit()

    calc = Calculation()
    calc.calculation(expression)


class Main:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b


Main = Main()
welcome()
calculate()