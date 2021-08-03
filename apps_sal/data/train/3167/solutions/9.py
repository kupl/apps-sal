def twos_difference(lst):
    newlist = lst
    even = []
    odd = []
    finaleven = []
    finalodd = []
    for num in newlist:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    for i in even:
        for j in even:
            if i + 2 == j:
                finaleven.append((i, j))
    for a in odd:
        for b in odd:
            if a + 2 == b:
                finalodd.append((a, b))
    y = sorted(finaleven)
    z = sorted(finalodd)
    return sorted(y + z)
