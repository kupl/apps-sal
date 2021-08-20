def get_strings(city):
    city = list(city.lower())
    if ' ' in city:
        for _ in range(city.count(' ')):
            city.remove(' ')
    r = ''
    while len(city):
        w = city[0]
        r += str(w) + ':' + '*' * int(city.count(w)) + ','
        for _ in range(city.count(w)):
            city.remove(w)
    return r[:-1]
