from collections import Counter


def get_strings(city):
    return ','.join((f"{letter}:{'*' * count}" for (letter, count) in list(Counter(city.lower()).items()) if letter != ' '))
