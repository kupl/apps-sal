import math
import re


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def para_to_rect(eqn1, eqn2):
    try:
        x_t = int(re.findall('\\-?\\d+?t', eqn1.replace('-t', '-1t'))[0].split('t')[0])
    except:
        x_t = 1
    try:
        y_t = int(re.findall('\\-?\\d+?t', eqn2.replace('-t', '-1t'))[0].split('t')[0])
    except:
        y_t = 1
    l = lcm(x_t, y_t)
    x_n = abs(l // x_t) * int(re.findall('\\-?\\d+$', eqn1.replace(' ', ''))[0])
    y_n = abs(l // y_t) * int(re.findall('\\-?\\d+$', eqn2.replace(' ', ''))[0])
    (x, y) = (l // abs(x_t), l // abs(y_t))
    if x_t * x + y_t * y == 0:
        return '{}x + {}y = {}'.format(x if x != 1 else '', y if y != 1 else '', x_n + y_n)
    return '{}x - {}y = {}'.format(x if x not in [1, -1] else '', y if y not in [1, -1] else '', x_n - y_n)
