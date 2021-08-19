import re


def evil(n):
    binary = '{0:b}'.format(n)
    return f"It's {('Evil' if len(re.findall('1', binary)) % 2 == 0 else 'Odious')}!"
