
def get_strings(city):
    city = city.replace(' ', '')
    city = city.lower()

    d = dict()
    for letter in city:
        if letter not in d:
            d[letter] = '*'
        else:
            d[letter] += '*'

    letter_list = list(map(lambda v: f'{v[0]}:{v[1]}', d.items()))
    return ','.join(letter_list)
