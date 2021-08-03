def get_strings(city):

    city = city.lower()
    result = ''

    for i in city:
        if not(i.isalpha()):
            pass
        elif i in result:
            pass
        else:
            result += f'{i}:{"*" * city.count(i)},'
    return result[:-1]
