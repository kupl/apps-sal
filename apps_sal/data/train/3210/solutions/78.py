def get_strings(city):
    city = city.lower()
    emptystr = ''
    for letter in city.lower():
        num = city.count(letter)
        if letter not in emptystr:
            if letter == ' ':
                continue
            elif letter is not city[-1]:
                emptystr += letter + ':' + str(num * '*') + ','
            else:
                emptystr += letter + ':' + str(num * '*') + ','
        else:
            pass
    if emptystr[-1] == ',':
        return emptystr[:-1]
    else:
        return emptystr
