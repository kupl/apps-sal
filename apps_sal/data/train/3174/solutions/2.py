from re import finditer, sub


def derivative(equation):
    mx = ''
    for exp in finditer('([\\+\\-])?(\\d*)?x\\^?(\\d+)?', equation):
        sign = -1 if exp.group(1) == '-' else 1
        scalar = int(exp.group(2)) if exp.group(2) else 1
        power = int(exp.group(3)) if exp.group(3) else 1
        mx += f'{sign * power * scalar}x^{power - 1}+'
    mx = sub('x\\^0\\b', '', mx)
    mx = sub('x\\^1\\b', 'x', mx)
    mx = sub('\\+\\-', '-', mx)
    if not mx:
        return '0'
    return mx[:-1]
