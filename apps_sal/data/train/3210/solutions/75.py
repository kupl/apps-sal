def get_strings(city):
    city = city.lower()
    emptystr = ''
    for letter in city.lower():
        num = city.count(letter)
        if letter not in emptystr:
            if letter == ' ':
                continue
            else:
                emptystr += letter + ':' + str(num * '*') + ','
        else:
            pass
    return emptystr[:-1]
