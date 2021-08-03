from collections import defaultdict
import re

P = re.compile(r'\+?(-?\d*)(x\^?)?(\d*)')


def differentiate(eq, x):

    derivate = defaultdict(int)
    for coef, var, exp in P.findall(eq):
        exp = int(exp or var and '1' or '0')
        coef = int(coef != '-' and coef or coef and '-1' or '1')

        if exp:
            derivate[exp - 1] += exp * coef

    return sum(coef * x**exp for exp, coef in derivate.items())
