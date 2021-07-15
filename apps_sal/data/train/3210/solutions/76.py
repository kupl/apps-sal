def get_strings(city):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    city_1 = ""
    for i in city:
        if i.lower() not in city_1 and i.isalpha():
            city_1 += i.lower()
        else:
            pass
    return ",".join('{}:{}'.format(i, '*' * city.lower().count(i)) for i in city_1)
