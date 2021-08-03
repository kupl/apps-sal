def get_strings(city):
    city = city.lower().replace(' ', '')
    return ','.join(f'{c}:' + '*' * (city.count(c)) for c in dict.fromkeys(city))
