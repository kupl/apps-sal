import re


def derivative(eq):
    monos = re.findall(r'([+-]?)(\d*)x\^?(\d*)', eq)
    result = ''
    for sign, coef, exp in monos:
        exp = int(exp or '1')
        coef = int(coef or '1') * exp
        result += f'{sign}{coef}x^{exp-1}'
    result = re.sub(r'x\^0|\^1\b', '', result)
    return result or '0'
