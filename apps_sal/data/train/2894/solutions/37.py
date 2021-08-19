def triple_trouble(one, two, three):
    result = ''
    for (i, c) in enumerate(one):
        result += c + two[i] + three[i]
    return result
