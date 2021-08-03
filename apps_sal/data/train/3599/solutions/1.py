def find_f1_eq_f2(n, k):
    s = set(range(k))
    while True:
        n += 1
        new = n
        while True:
            ns = set(map(int, str(new)))
            if ns < s:
                break
            elif ns == s:
                return n
            new += n
    return n
