def triple_trouble(one, two, three):
    i = 0
    t = ''
    while i < len(three):
        t = t + one[i] + two[i] + three[i]
        i += 1
    return(t)
