def triple_trouble(one, two, three):
    L = len(one)
    result = []
    for x in range(L):
        result.append(one[x])
        result.append(two[x])
        result.append(three[x])
    return "".join(result)
