def get_strings(city):
    cityDict = {}
    for i in city.lower():
        if i.isalpha():
            if i not in cityDict:
                cityDict[i] = 1
            else:
                cityDict[i] += 1
    
    chars = []
    for i in cityDict.keys():
        chars.append("{}:{}".format(i, '*' * cityDict[i]))
    
    return ','.join(chars)
