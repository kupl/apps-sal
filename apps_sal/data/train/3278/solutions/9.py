def string_expansion(s):
    from re import findall
    result = findall('^[a-zA-Z]*', s)[0]
    for i in findall('(\d)([a-zA-Z]+)', s):
        for j in i[1]:
            result += j*int(i[0])
    return result
