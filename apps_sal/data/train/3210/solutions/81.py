def get_strings(city):
    lettercount = []
    check = ''
    for i in city.lower():
        if i not in check and i.isalpha():
            check = check + i
            string = '{}:{}'.format(i, city.lower().count(i) * '*')
            lettercount.append(string)
    return ','.join(lettercount)
