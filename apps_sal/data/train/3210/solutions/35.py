from collections import OrderedDict


def get_strings(city):
    return ','.join((f"{letter}:{'*' * city.lower().count(letter)}" for letter in {letter: None for letter in city.lower() if letter.isalpha()}))
