def combos(n):
    mom_a = [[1]]
    i = 2
    while i <= n:
        tmp_a = [[i]]
        for lst in mom_a:
            tmp_a.insert(0, [1] + lst)
        for lst in mom_a:
            for j in range(len(lst)):
                tmp_lst = sorted(lst[:j] + [lst[j] + 1] + lst[j + 1:])
                if not tmp_lst in tmp_a:
                    tmp_a.append(tmp_lst)
        mom_a = tmp_a
        i += 1
    return mom_a
