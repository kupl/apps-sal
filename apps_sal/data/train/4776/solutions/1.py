def u_list(index):
    out = [1, 1]
    for i in range(2, index):
        out.append(out[i - out[-1]] + out[i - out[-2]])
    return out


def length_sup_u_k(n, k):
    return sum([1 for x in u_list(n) if x >= k])


def comp(n):
    us = u_list(n)
    return sum([1 for i in range(n - 1) if us[i] > us[i + 1]])
