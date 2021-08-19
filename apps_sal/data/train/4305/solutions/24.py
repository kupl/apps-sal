def order_weight(strng):
    res = strng.split(' ')
    list = []
    for x in res:
        a = 0
        res2 = [z for z in x]
        for y in res2:
            a += int(y)
        list.append(a)
    answer = [m for (n, m) in sorted(zip(list, res))]
    return ' '.join(answer)
