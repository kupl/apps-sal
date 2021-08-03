def score_pole_vault(vaulter_list):
    popytki = len(vaulter_list[0]["results"])
    temp = {}
    res = {}
    for mas in vaulter_list:
        i = popytki - 1
        while i >= 0 and mas["results"][i].find('O') == -1:
            i -= 1
        if i < 0:
            n = 0
            m = ''.join(mas["results"]).count('X')
        else:
            n = mas["results"][i].count('X')
            m = ''.join(mas["results"][:i]).count('X')
        new_key = (popytki - i, n, m)
        temp[new_key] = temp.get(new_key, []) + [mas["name"]]
    k = iter(sorted(temp))
    i = 0
    while i < 3:
        key = next(k)
        if i == 0 and len(temp[key]) == 1:
            res['1st'] = temp[key][0]
            i += 1
        elif i == 0 and len(temp[key]) > 1:
            res['1st'] = ', '.join(sorted(temp[key])) + ' (jump-off)'
            i += len(temp[key])
        elif i == 1 and len(temp[key]) == 1:
            res['2nd'] = temp[key][0]
            i += 1
        elif i == 1 and len(temp[key]) > 1:
            res['2nd'] = ', '.join(sorted(temp[key])) + ' (tie)'
            i += len(temp[key])
        elif i == 2 and len(temp[key]) == 1:
            res['3rd'] = temp[key][0]
            i += 1
        elif i == 2 and len(temp[key]) > 1:
            res['3rd'] = ', '.join(sorted(temp[key])) + ' (tie)'
            i += len(temp[key])
    return res
