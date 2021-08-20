from collections import Counter


def get_strings(city):
    c = Counter(list(filter(str.isalpha, city.lower())))
    return ','.join((f"{char}:{'*' * freq}" for (char, freq) in list(c.items())))
