def get_strings(city):
    dic = dict()
    for c in city.lower():
        if c.isalpha and c != " ":
            dic[c] = dic.get(c, 0) + 1
    result = list()
    for key, value in dic.items():
        result.append('{}:{}'.format(key, value * '*'))
    out = ','.join(result)
    return out
