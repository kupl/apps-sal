def jumbled_string(s, n):
    def mixer(s): return s[::2] + s[1::2]

    if n == 1:
        return mixer(s)

    cnt = 1
    x = s
    while s != mixer(x):
        cnt += 1
        x = mixer(x)

    max = n % cnt
    while max != 0:
        s = mixer(s)
        max -= 1
    return s
