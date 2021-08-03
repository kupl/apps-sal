def triple_trouble(one, two, three):

    counter = 0
    res = ''
    for i in one:
        res += i
        res += two[counter]
        res += three[counter]
        counter += 1
    return res
