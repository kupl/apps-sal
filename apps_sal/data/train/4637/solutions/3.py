import re
from math import ceil

P_RECIPE = re.compile(r'([\d/]+) (tb?sp)')


def convert_recipe(recipe): return P_RECIPE.sub(update, recipe)


def update(m):
    toGrams = ceil(eval(m.group(1)) * (15 if m.group(2) == 'tbsp' else 5))
    return "{} {} ({}g)".format(m.group(1), m.group(2), toGrams)
