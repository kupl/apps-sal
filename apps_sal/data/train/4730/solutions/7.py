def prime_bef_aft(num):
    res = []
    for i in range(num, 0, -1):
        if len([x for x in range(1, i+1) if i % x == 0 and i != num]) == 2:
            res.append(i)
            break
    i = num
    while len(res) != 2:
        i += 1
        if len([x for x in range(1, i+1) if i % x == 0 and i != num]) == 2:
            res.append(i)
            break
    return res

