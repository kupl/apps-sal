def get_strings(city):
    city = city.lower()
    res = []
    for x in city:
        c = city.count(x)
        st = f"{x}:{'*'*c}"
        if x.isalpha() and not st in res:
            res.append(st)
    return ",".join(res)
