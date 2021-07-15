def triple_trouble(one, two, three):
    ret = ""
    for i in range(len(one)):
        ret = ret + one[i] + two[i] + three[i]
    return ret
