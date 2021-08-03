def consecutive_sum(num):
    count = 0
    N = 1
    while(N * (N + 1) < 2 * num):
        a = (num - (N * (N + 1)) / 2) / (N + 1)
        if (a - int(a) == 0.0):
            count += 1
        N += 1
    return count + 1
