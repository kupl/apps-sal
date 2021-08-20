from collections import Counter


def get_strings(city):
    return ','.join((f"{e}:{'*' * c}" for (e, c) in Counter(city.lower()).items() if e.isalpha()))
