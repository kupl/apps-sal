import re
import math


def convert_recipe(recipe):
    r = re.sub('((\\d+(/\\d+)?) tbsp)', tbsp, recipe)
    r = re.sub('((\\d+(/\\d+)?) tsp)', tsp, r)
    return r


def tbsp(m):
    return m.group(1) + ' (' + str(math.ceil(eval('15*' + m.group(2)))) + 'g)'


def tsp(m):
    return m.group(1) + ' (' + str(math.ceil(eval('5*' + m.group(2)))) + 'g)'
