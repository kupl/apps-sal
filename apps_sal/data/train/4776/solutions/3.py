def length_sup_u_k(n, k):
    u = {1: 1, 2: 1}

    count = 0
    if k == 1:
        count += 2
    for i in range(3, n + 1):
        u[i] = u[i - u[i - 1]] + u[i - u[i - 2]]
        if u[i] >= k:
            count += 1
    return count


def comp(n):
    u = {1: 1, 2: 1}
    count = 0
    for i in range(3, n + 1):
        u[i] = u[i - u[i - 1]] + u[i - u[i - 2]]
        if u[i] < u[i - 1]:
            count += 1
    return count
