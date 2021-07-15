def find_num(n):
    seq = [0]
    i = 0
    while i < n:
        a = seq[-1]
        b = next(x for x in list(range(n*3))
                 if all(y not in str(x) for y in list(str(a)))
                 and x not in seq)
        seq.append(b)
        i += 1
    return seq[-1]
