def get_strings(city):
    dict = {}
    for c in city.lower():
        if not c.isspace():
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
    out = ''
    count = 1
    for x in dict:
        out += x + ':' + dict[x] * '*'
        if count != len(dict):
            out += ','
        count += 1
    return out
