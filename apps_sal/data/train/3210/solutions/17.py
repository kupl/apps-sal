from collections import Counter


def get_strings(city):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    city_str = ''
    city_dict = Counter(city.lower())
    for key in city_dict:
        if key in alphabet:
            city_str += key + ':' + '*' * city_dict[key] + ','
    return city_str[:-1]
