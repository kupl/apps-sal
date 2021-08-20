def string_func(s, x):
    if not x:
        return s
    k = [s]
    new_s = list(s)
    while True:
        (new_s[::2], new_s[1::2]) = (new_s[:len(new_s) // 2 - 1:-1], new_s[:len(new_s) // 2])
        k.append(''.join(new_s))
        if k[-1] == s:
            return k[x % (len(k) - 1)]
