def get_strings(city):
    result = ''
    city = city.lower().replace(' ', '')
    for i in city:
        if i not in result:
            result += f"{i}:{'*' * city.count(i)},"
    return result[:-1]
