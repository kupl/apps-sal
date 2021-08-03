def get_strings(city):
    formatRes = ""
    string = ""
    newCity = city.lower().replace(' ', '')
    main = {}
    i = 0
    k = 0
    while i < len(newCity):
        if main.get(newCity[i]):
            bef = main[newCity[i]]
            main[newCity[i]] = bef + "*"
            i += 1
        else:
            main[newCity[i]] = "*"
            formatRes += newCity[i]
            i += 1
    while k < len(formatRes):
        string = string + formatRes[k] + ":" + main[formatRes[k]] + ","
        k += 1
    return string[:-1]
