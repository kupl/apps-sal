from math import factorial


def strong_num(number: int) -> str:
    return 'STRONG!!!!' if number == sum(map(factorial, list(map(int, str(number))))) else 'Not Strong !!'
