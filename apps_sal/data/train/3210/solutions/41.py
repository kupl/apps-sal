
def get_strings(city):
    new = city.lower().replace(' ', '')

    list = []
    for x in new:
        c = new.count(x)
        y = x + ":" + "*" * c
        if y not in list:
            list.append(y)

        s = ','.join(list)

    return s
