from math import factorial
facts = {factorial(n): n for n in range(1000)}


def reverse_factorial(num):
    res = facts.get(num, 0)
    return '%s!' % res if res else 'None'
