from collections import Counter


def get_strings(city):
    count = Counter(city.lower().replace(' ', ''))
    return ','.join([f"{k}:{'*' * v}" for (k, v) in count.items()])
