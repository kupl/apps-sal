def mem_alloc(banks):
    banks = banks[:]
    d = set()
    n = 0
    L = len(banks)
    while tuple(banks) not in d:
        d |= {tuple(banks)}
        n += 1
        i, m = 0, 0
        for j, v in enumerate(banks):
            if v > m:
                m = v
                i = j
        a, b = divmod(m, L)
        banks[i] = 0
        for _ in range(L):
            banks[_] += a
        for _ in range(b):
            banks[(i + _ + 1) % L] += 1
    return n
