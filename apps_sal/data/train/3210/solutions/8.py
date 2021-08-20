import re


def get_strings(city):
    cache = {}
    r_string = ''
    counter = 0
    city = re.sub(' ', '', city)
    for letter in city.lower():
        if letter not in cache:
            cache[letter] = 0
            cache[letter] += 1
        else:
            cache[letter] += 1
    for (k, v) in cache.items():
        if counter < len(cache) - 1:
            r_string += k + ':' + '*' * v + ','
            counter += 1
        elif counter < len(cache):
            r_string += k + ':' + '*' * v
    return r_string
