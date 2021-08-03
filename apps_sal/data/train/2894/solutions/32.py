def triple_trouble(one, two, three):
    result = ""
    n = 0
    while n < len(one):
        result += one[n] + two[n] + three[n]
        n += 1

    return result
