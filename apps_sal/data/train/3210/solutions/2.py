def get_strings(city):
    city = city.lower()
    result = ""
    for i in city:
        if i in result:
            pass
        elif i == " ":
            pass
        else:
            result += i + ":" + ("*" * city.count(i)) + ","

    return result[:-1]
