from constants import *


def calculate(num1, operator, num2):
    if operator not in ('ADD', 'SUB', 'MUL', 'DIV'):
        print("wrong operation")
    if operator == 'ADD':
        print(num1 + num2)
    if operator == 'SUB':
        print(num1 - num2)
    if operator == 'MUL':
        print(num1 * num2)
    if operator == 'DIV':
        if num2 != 0:
            print(num1 / num2)
        else:
            print("You can't divide by 0")
