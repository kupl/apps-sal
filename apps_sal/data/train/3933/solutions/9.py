from re import compile

REGEX = compile(r"\d+").findall


def hydrate(drink_string):
    res = sum(map(int, REGEX(drink_string)))
    return f"{res} glass{'es'*(res != 1)} of water"
