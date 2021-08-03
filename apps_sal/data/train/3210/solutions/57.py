def get_strings(city):
    formatedS = city.replace(' ', '').lower()
    res = ""
    count = 1
    for x, c in enumerate(formatedS):
        for d in formatedS[x + 1:]:
            if(d == c):
                count += 1
        if c not in res:
            res += c + ":" + "*" * count + ","
        count = 1
    return res[:-1]
