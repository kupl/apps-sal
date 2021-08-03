import math


def solve(sum, gcd):
    for firstNumber in (number for number in range(1, sum) if number % gcd is 0):
        secondNumber = sum - firstNumber
        if secondNumber % gcd is 0:
            return (firstNumber, secondNumber)
    return -1
