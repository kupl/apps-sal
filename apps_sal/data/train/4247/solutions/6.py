def odd(s):
    odds = list(s)
    for i in odds:
        if i != 'o' and i != 'd':
            odds.remove(i)
    x = 3
    num = 0
    t = 0
    flag = True
    m = [2, 1]
    l_index = []
    while x == 3:
        if flag == False:
            odds[0:l_index[0]]
            for i in l_index:
                odds.pop(i - t)
                t = t + 1
            x = 0
            t = 0
            num = num + 1
            l_index = []
            index = 0
        else:
            x = 0
            index = 0
        for i in odds:
            if x == 0 and i == 'o':
                x = x + 1
                l_index.append(index)
            elif x in m and i == 'd':
                x = x + 1
                l_index.append(index)
                flag = False
            index = index + 1
    return num
