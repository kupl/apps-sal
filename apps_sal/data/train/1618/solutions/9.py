def differentiate(equation, point):
    if equation[0] != '-':
        equation = '+' + equation
    equation = equation.replace('+x', '+1x').replace('-x', '-1x').replace('+', ' ').replace('-', ' -')
    terms = [[int(e) for e in (w + '^1' if '^' not in w else w).split('x^')] for w in equation.split() if 'x' in w]
    return sum((c * p * point ** (p - 1) for (c, p) in terms))
