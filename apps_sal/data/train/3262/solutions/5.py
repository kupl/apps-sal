from collections import defaultdict


def key(s):
    s = s.lower().replace(' ', '')
    return min((s[i:] + s[:i] for i in range(len(s))))


def group_cities(seq):
    result = defaultdict(list)
    for city in set(seq):
        result[key(city)].append(city)
    for cities in result.values():
        cities.sort()
    return sorted(result.values(), key=lambda cities: (-len(cities), cities[0]))
