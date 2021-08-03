def get_strings(city):
    print(city)
    city, m, mas, l = city.lower(), "", [], []
    for i in set(city.lower()):
        if city.count(i) > 1:
            mas.append(i)
            l.append(city.count(i))
            for j in range(city.count(i) - 1):
                city = city[:city.rindex(i)] + city[city.rindex(i) + 1:]
    for i in city:
        if i in mas:
            m += i + ":" + "*" * l[mas.index(i)] + ","
        elif i != " ":
            m += i + ":*" + ","
    return m[:len(m) - 1]
