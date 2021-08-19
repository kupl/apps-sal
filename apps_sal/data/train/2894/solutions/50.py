def triple_trouble(one, two, three):
    result = ''
    x = 0
    for i in one:
        result = result + i + two[x] + three[x]
        x = x + 1
    return result
