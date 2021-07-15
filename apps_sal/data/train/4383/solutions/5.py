def artificial_rain(garden):
    if len(garden) < 20:
        print(garden)
    res = 0
    last = 0
    m = -1
    k = 0
    while garden:
        while garden and garden[0] >= last:
            last = garden.pop(0)
            res += 1
        while garden and garden[0] <= last:
            if garden[0] == last:
                k += 1
            if garden[0] < last:
                k = 0
            res += 1
            last = garden.pop(0)
        m = max(res, m)
        res = k+1
    m = max(res, m)
    return m
