def get_strings(city):
    myMap = {}
    for i in range(len(city)):
        letter = city[i].lower()
        if letter not in myMap:
            myMap[letter] = 1
        else:
            myMap[letter] = myMap.get(letter) + 1
    myMap.pop(' ', None)
    result = ''
    for item in myMap:
        result = result + item + ':'
        for i in range(myMap.get(item)):
            result += '*'
        result += ','
    return result[:-1]
