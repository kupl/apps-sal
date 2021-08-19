from math import factorial


def strong_num(n):
    print(n)
    return ['Not Strong !!', 'STRONG!!!!'][n == sum(map(factorial, [int(x) for x in str(n)]))]
