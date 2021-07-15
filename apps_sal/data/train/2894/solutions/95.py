def triple_trouble(one, two, three):
    result = ""
    e = 0
    while e < len(one):
        result += one[e] + two[e] + three[e]
        e += 1
    return result
