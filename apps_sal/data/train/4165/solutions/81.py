def uni_total(string):
    tot = 0
    for x in list(string):
        tot += ord(x)
    return tot
