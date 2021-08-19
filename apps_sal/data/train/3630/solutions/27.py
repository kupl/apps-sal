def arithmetic(a: int, b: int, operator: str) -> int:
    """ Get the result of the two numbers having the operator used on them. """
    return {'add': lambda: a + b, 'subtract': lambda: a - b, 'multiply': lambda: a * b, 'divide': lambda: a / b}.get(operator)()
