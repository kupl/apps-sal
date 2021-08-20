def get_strings(city):
    string = []
    for i in city.lower():
        n = city.lower().count(i)
        if i + ':' + '*' * n not in string and i.isalpha():
            string.append(i + ':' + '*' * n)
    return ','.join(string)
