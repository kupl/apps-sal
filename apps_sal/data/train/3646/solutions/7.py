def fixed_points_perms(n, k):
    fact_list = [0, 1]
    dearr_list = [1, 0]
    if k == n:
        return 1
    elif k > n:
        return 0

    if k != 0:
        for i in range(2, n + 1):
            fact_list.append(i * fact_list[-1])
        combinations = fact_list[-1] // (fact_list[k] * fact_list[n - k])
    else:
        combinations = 1

    for i in range(2, n - k + 1):
        dearr_list.append((i - 1) * (dearr_list[-1] + dearr_list[-2]))
    print(combinations, dearr_list[-1])
    return int(combinations) * dearr_list[-1]
