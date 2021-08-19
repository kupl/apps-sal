def parse_monom(monom):
    if 'x' not in monom:
        monom = monom + 'x^0'
    if monom.startswith('x'):
        monom = '1' + monom
    if monom.startswith('-x'):
        monom = '-1' + monom[1:]
    if monom.endswith('x'):
        monom = monom + '^1'
    (coefficient, degree) = map(int, monom.replace('x', '').split('^'))
    return (degree, coefficient)


def differentiate(equation, point):
    monoms = equation.replace('-', '+-').lstrip('+').split('+')
    polynom = dict(map(parse_monom, monoms))
    return sum((coefficient * degree * point ** (degree - 1) for (degree, coefficient) in polynom.items() if degree))
