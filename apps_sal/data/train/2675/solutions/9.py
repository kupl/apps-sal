def bad_apples(apples):
    a = apples[:]
    for i in range(len(a) - 1):
        if a[i].count(0) == 1:
            for j in range(i + 1, len(a)):
                if a[j].count(0) == 1:
                    a[i] = [sum(a[i]), sum(a[j])]
                    a[j] = [0, 0]
                    break
    return [i for i in a if 0 not in i]
