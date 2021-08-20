def triple_trouble(one, two, three):
    result = []
    for (pt1, pt2, pt3) in zip(one, two, three):
        for (i, j, k) in zip(pt1, pt2, pt3):
            result.append(i)
            result.append(j)
            result.append(k)
    return ''.join(result)
