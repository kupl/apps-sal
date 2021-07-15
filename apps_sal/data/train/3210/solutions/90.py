def get_strings(city):
    city = city.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    city_dict = {}
    for char in city:
        if char not in alpha: continue
        if char in city_dict:
            city_dict[char] += '*'
            continue
        city_dict[char] = '*'
    output = ''
    for k in city_dict:
        output += f'{k}:{city_dict[k]},'
    return output[0:-1]

