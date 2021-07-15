from math import ceil
import re


def convert_recipe(recipe):
    spoons = set(re.findall(r"[^ ]+ tb?sp", recipe))
    for spoon in spoons:
        qty, typ = spoon.split(" ")
        wgt = ceil({"tsp": 5, "tbsp": 15}[typ] * eval(qty))
        recipe = re.sub(f"(^| ){spoon}", f"\g<1>{spoon} ({wgt}g)", recipe)
    return recipe
