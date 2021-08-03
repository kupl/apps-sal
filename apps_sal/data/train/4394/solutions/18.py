def men_still_standing(cards):
    if cards == []:
        return (11, 11)
    a, b = [1] * 11, [1] * 11
    dicA, dicB = {}, {}
    for i in cards:
        if i[-1] == 'Y':
            if i[:-1] in dicA:
                a[dicA[i[:-1]] - 1] = 0
            elif i[:-1] in dicB:
                b[dicB[i[:-1]] - 1] = 0
            else:
                if i[0] == 'A':
                    dicA[i[:-1]] = int(i[1:-1])
                else:
                    dicB[i[:-1]] = int(i[1:-1])
        elif i[-1] == 'R':
            if i[0] == 'A':
                a[int(i[1:-1]) - 1] = 0
            elif i[0] == 'B':
                b[int(i[1:-1]) - 1] = 0
        if sum(a) == 6 or sum(b) == 6:
            return (sum(a), sum(b))
    return (sum(a), sum(b))
