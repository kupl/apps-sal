import re
import math


def convert_recipe(recipe):
    return re.sub('(\\d+\\/\\d+|\\d+) (tbsp|tsp)', lambda x: x.group(1) + ' ' + x.group(2) + ' ' + '(' + str(math.ceil(eval(x.group(1)) * {'tbsp': 15, 'tsp': 5}[x.group(2)])) + 'g)', recipe)
