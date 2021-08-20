def get_strings(city):
    return ','.join([i + ':' + '*' * city.lower().count(i) for i in dict.fromkeys(city.lower().replace(' ', ''))])
