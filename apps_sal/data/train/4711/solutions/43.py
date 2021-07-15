def zeros(n):
    num_5 = n
    num_2 = n
    n_5 = 0
    n_2 = 0
    while num_5 != 0:
        n_5 += num_5 // 5
        num_5 = num_5 // 5
    return n_5
