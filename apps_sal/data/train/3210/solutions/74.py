def get_strings(city):
    dic = {}
    city = city.lower()
    for i in range(len(city)):
        if city[i] != " ":
            dic[city[i]] = city.count(city[i])
    output: str = ','.join("{}:{}".format(key, val * "*") for (key, val) in list(dic.items()))
    return output
