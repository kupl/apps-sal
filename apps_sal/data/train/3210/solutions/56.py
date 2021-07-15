def get_strings(city):
    result = {}
    for i in city.lower():
        if i in result and i != " ":
            result[i] += "*"
        elif i not in result and i != " ":
            result[i] = "*"
    test = []
    for k, v in list(result.items()):
        test.append((k+':'+v))
    return ",".join(test)
    

