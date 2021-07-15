def get_char_count(s):
    newDict = {}
    s = s.lower()
    s = "".join(sorted(s))
    for element in s:
        if element.isalnum():
            newDict.setdefault(element, 0)
            newDict[element] += 1
    inverse = {}
    for key in newDict:
        value = newDict[key]
        inverse.setdefault(value, []).append(key)
    return inverse
        

