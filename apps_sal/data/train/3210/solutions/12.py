def get_strings(city):
    index = 0
    string = ''
    city = city.lower()
    city = city.replace(' ', '')
    for i in city:
        asterisks = city.count(i)
        if i in string:
            index = index + 1
        else:
            if index == (len(city) - 1) and i not in string:
                string += i.lower() + ':' + ('*' * asterisks)
            if index != (len(city) - 1):
                string += i.lower() + ':' + ('*' * asterisks) + ','
                index = index + 1
    if string[-1] == ',':
        lst = list(string)
        lst[-1] = ''
        new = ''.join(lst)
        return new
    return string
