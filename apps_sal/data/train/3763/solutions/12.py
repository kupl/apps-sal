from typing import Union


def calculator(x: int, y: int, op: str) -> Union[int, float, str]:
    """ Make a calculation two values based on the given operator. """
    calculate = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    if all([type(x) is int, type(y) is int]):
        try:
            return calculate[op](x, y)
        except KeyError:
            pass
    return 'unknown value'
