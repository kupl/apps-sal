r = [0]


def min_length_num(num_dig, ord_max):
    for n in range(1, ord_max + 1):
        if n < len(r):
            s = r[n]
        else:
            s = 0
            for i in range(1, n):
                s += i ** (n - i)
            r.append(s)
        if len(str(s)) == num_dig:
            return [True, n]
        elif len(str(s)) > num_dig:
            return [False, -1]
    return [False, -1]
