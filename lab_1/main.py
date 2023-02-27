from constants import *
from calculate import calculate
from print_hello import print_hello
from even_numbers import even_numbers


if __name__ == '__main__':
    print_hello()

    num1 = float(input('firstNum = '))
    operation = input('Operation: ')
    num2 = float(input('secondNum = '))
    calculate(num1, operation, num2)

    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(even_numbers(list_1))