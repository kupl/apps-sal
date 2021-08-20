def get_strings(city):
    city = ''.join(city.lower().split())
    res = []
    letters = []
    for letter in city:
        if letter not in letters:
            res.append(str(letter + ':' + '*' * city.count(letter)))
            letters.append(letter)
    return ','.join(res)
