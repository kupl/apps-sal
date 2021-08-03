def get_strings(city):
    city = city.lower()
    storage = []
    hold = ""
    for i in (city):
        if i.isalpha() == True and str(i) not in hold:
            storage.append(str(i) + ':' + (city.count(i)) * '*')
            hold += str(i)
    return ",".join(storage)
