from math import factorial as f


def strong_num(n):
    return ['Not Strong !!', 'STRONG!!!!'][sum((f(i) for i in map(int, str(n)))) == n]
