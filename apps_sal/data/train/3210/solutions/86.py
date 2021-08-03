def get_strings(city):
    z = str()
    city = city.replace(" ", "").lower()
    for i in city:
        cnt = int(city.count(i))
        j = 1
        y = ''
        if z.find(i) == -1:
            y = i + ':'
            while j <= cnt:
                y = y + '*'
                j = j + 1
            y = y + ','
        z = z + y

    return z[:-1]
