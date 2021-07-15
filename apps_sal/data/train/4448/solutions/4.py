def get_derivative(string):
    if not 'x' in string:
        return '0'
    if not '^' in string:
        return string[:-1]
    coef, exp = list(map(int, string.split('x^')))
    return f"{coef * exp}x^{exp - 1}" if exp != 2 else f"{coef * exp}x"

