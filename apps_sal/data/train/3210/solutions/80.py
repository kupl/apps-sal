def get_strings(city):
    dict_letters = {}
    for i in city.replace(' ', '').lower():
        if i in dict_letters:
            dict_letters[i] += '*'
        else:
            dict_letters[i] = '*'
    string_counts = ''
    for (k, v) in dict_letters.items():
        string_counts += k + ':' + v + ','
    return string_counts[:-1]
