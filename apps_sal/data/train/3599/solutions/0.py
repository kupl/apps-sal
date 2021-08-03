def find_f1_eq_f2(n, k):
    s = set(range(k))
    while True:
        n += 1
        testn = n
        while True:
            f = set(map(int, str(testn)))
            if f <= s:
                if f == s:
                    return n
                break
            testn += n
