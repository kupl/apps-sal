import re


def hydrate(drink_string):
    drink = sum(int(n) for n in re.findall(r"\d", drink_string))
    return f"{drink} glass{'es' if drink > 1 else ''} of water"
