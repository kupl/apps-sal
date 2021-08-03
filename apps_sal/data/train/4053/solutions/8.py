from math import factorial as fact
D = {fact(v): '{}!'.format(v) for v in range(1, 16)}


def reverse_factorial(num):
    return D.get(num, 'None')
