def men_from_boys(arr):
    l1 = []
    l2 = []
    for i in sorted(set(arr)):
        if i % 2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    return l1 + l2[::-1]
