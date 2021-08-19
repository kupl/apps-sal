def length_sup_u_k(n, k):
    return sum((i >= k for i in u(n)))


def comp(n):
    ui = u(n)
    return sum((x > y for (y, x) in zip(ui[1:], ui[:-1])))


def u(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        seq = [1, 1]
        for i in range(2, n):
            seq.append(seq[i - seq[i - 1]] + seq[i - seq[i - 2]])
        return seq
