def get_strings(city):
    city = city.lower().replace(" ", "")
    return ",".join(sorted([f"{i}:{city.count(i)*'*'}" for i in set(city)], key=lambda x:city.index(x[0])))
