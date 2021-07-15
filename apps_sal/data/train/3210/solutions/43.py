def get_strings(city):
    res = {}
    for x in city.lower():
        if x.isalpha():
            res[x] = city.lower().count(x)
    return ",".join([ "%s:%s" % (x,"*"*res[x]) for x in res])
