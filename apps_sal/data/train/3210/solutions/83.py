def get_strings(city):
    city = city.lower()
    c = []
    b = []
    for ans in city:
        if ans not in b and ans != " ":
            b += ans
            c += [ans + ":" + city.count(ans) * "*"]
    return ",".join(c)
