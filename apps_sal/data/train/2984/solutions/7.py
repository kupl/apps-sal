def infected_zeroes(lst):
    duzinaNiza = len(lst)
    if duzinaNiza == 1:
        return 0
    result = 0
    clanNiza = lst[0]
    br_out = 0
    i = 0
    br_poc = 0
    br_kraj = 0
    while clanNiza == 1:
        br_out += 1
        i += 1
        clanNiza = lst[i]
    br_poc = br_out
    clanNiza = lst[duzinaNiza - 1]
    br_out = 0
    j = duzinaNiza - 1
    while clanNiza == 1:
        br_out += 1
        j -= 1
        clanNiza = lst[j]
    br_kraj = br_out
    br_in = 0
    br_sred_par = 0
    br_sred_nepar = 0
    for k in range(i + 1, j + 1):
        if lst[k] == 1:
            br_in += 1
        elif br_in % 2 == 0:
            if br_sred_par <= br_in:
                br_sred_par = br_in
                br_in = 0
        elif br_sred_nepar <= br_in:
            br_sred_nepar = br_in
            br_in = 0
    maxOut = 0
    maxIn = 0
    if br_poc > br_kraj:
        maxOut = br_poc
    else:
        maxOut = br_kraj
    if br_sred_nepar > br_sred_par:
        maxIn = br_sred_nepar
    else:
        maxIn = br_sred_par
    if maxIn % 2 == 0:
        if maxIn / 2 >= maxOut:
            return maxIn // 2
        else:
            return maxOut
    elif maxIn // 2 + 1 >= maxOut:
        return maxIn // 2 + 1
    else:
        return maxOut
