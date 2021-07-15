def get_strings(city):
    city = city.lower().replace(" ", "")
    arr = []
    for el in city:
        if el not in arr:
            arr.append(el)
    return ",".join([f"{el}:{city.count(el) * '*'}" for el in arr])
