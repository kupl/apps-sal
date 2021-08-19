from collections import Counter


def get_strings(city):
    counts = Counter(city.replace(' ', '').lower())
    return ','.join([f"{x}:{'*' * counts[x]}" for x in counts])
