def get_strings(city):
    city = city.lower().replace(' ', '')
    dict = {}
    for l in city:
        if l in dict:
            dict[l] += '*'
        else:
            dict[l] = '*'
    result = ''
    for i in dict:
        result += i + ':' + dict[i] + ','
    return result[:-1]
