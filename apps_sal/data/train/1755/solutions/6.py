def splitlist(lst):
    dicto = {}

    def spliteer(lst, sum1=0, sum2=0, ls1=[], ls2=[], i=0):
        key = f'{sum1}{i}'
        if key in dicto:
            return dicto[key]
        if i >= len(lst):
            return (abs(sum1 - sum2), [ls1, ls2])
        else:
            min1 = spliteer(lst, sum1 + lst[i], sum2, ls1 + [lst[i]], ls2, i + 1)
            min2 = spliteer(lst, sum1, sum2 + lst[i], ls1, ls2 + [lst[i]], i + 1)
            dicto[key] = min(min1, min2, key=lambda x: x[0])
        return dicto[key]
    return spliteer(lst)[1]
