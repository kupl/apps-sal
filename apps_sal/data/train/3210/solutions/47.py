def get_strings(city):
    city = city.lower().replace(' ', '')
    a = []
    for el in city:
        if el not in a:
            a.append(el)
    return ','.join([f"{el}:{'*' * city.count(el)}" for el in a])
