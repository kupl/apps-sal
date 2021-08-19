def get_strings(city):
    city = city.lower()
    city = city.replace(' ', '')
    cit_str = ''
    usedletters = []
    for letter in city:
        if letter in usedletters:
            pass
        else:
            cit_str += letter + ':'
            l_num = city.count(letter)
            for num in range(0, l_num):
                cit_str += '*'
            cit_str += ','
            usedletters.append(letter)
    return cit_str[:-1]
