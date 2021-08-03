def get_strings(city):

    city = city.replace(' ', '').lower()
    city_string = ''

    for i in city:
        if i in city_string:
            pass
        else:
            city_string += i + ':' + ('*' * city.count(i)) + ','

    result = city_string[:-1]

    return result
