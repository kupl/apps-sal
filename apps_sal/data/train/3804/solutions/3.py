def S(n):
    s = 0
    for i in range(1, n):
        s = s + i ** (n - i)
    return s


x = [len(str(S(n))) for n in range(1000)]


def min_length_num(num_dig, ord_max):
    y = x[1:ord_max + 1]
    if not num_dig in y:
        return [False, -1]
    for i in range(len(y) + 1):
        if y[i] >= num_dig:
            return [True, i + 1]
