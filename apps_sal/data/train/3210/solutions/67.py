from collections import OrderedDict


def get_strings(city):
    city = city.lower().replace(' ', '')
    city_short = ''.join(OrderedDict.fromkeys(city))
    city_string = ''
    for (char1, char2) in zip(city, city_short):
        value = city.count(char2)
        city_string += f"{char2}:{value * '*'},"
    city_string = city_string[:-1]
    return city_string
