def get_strings(city):
    city = list(city.lower())
    con = {}
    for char in city:
        if char == ' ':
            pass
        else:
            con[char] = city.count(char) * '*'
    first = True
    result = ''
    for item in con.keys():
        if first == True:
            first = False
            result += item + ':' + con.get(item)
        else:
            result += ',' + item + ':' + con.get(item)
    return result
