def get_strings(city):
    city = city.lower()
    city = list(city)
    dicti = {}
    strres = ""

    for i in city:
        if ord(i) > 96 and ord(i) < 123:
            if i in dicti:
                dicti[i] += 1
            else:
                dicti[i] = 1

    for i in dicti:
        strres = strres + i + ":" + ("*" * dicti[i]) + ","

    strres = strres[:-1]

    return strres
