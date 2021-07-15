import re
from math import ceil
from fractions import Fraction

def convert(m, units={'tbsp': 15, 'tsp': 5}):
    amount, unit = m.groups()
    gram = int(ceil(Fraction(amount) * units[unit]))
    return f'{m.group()} ({gram}g)'

def convert_recipe(recipe):
    return re.sub('(\S+) (tb?sp)', convert, recipe)
