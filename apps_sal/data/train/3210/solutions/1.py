from collections import Counter


def get_strings(city):
    return ','.join((f"{char}:{'*' * count}" for (char, count) in list(Counter(city.replace(' ', '').lower()).items()) if char.isalpha()))
