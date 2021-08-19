def get_strings(city):
    c = {}
    for i in city.lower():
        if i == ' ':
            continue
        try:
            c[i] += 1
        except:
            c[i] = 1
    res = ''
    for (i, j) in c.items():
        res += i + ':' + '*' * j + ','
    return res[:len(res) - 1]
