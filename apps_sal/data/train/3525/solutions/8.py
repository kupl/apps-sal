def flipping_game(a):
    m = 0
    for i in range(len(a)):
        for j in range(i, len(a) + 1):
            x = sum(a[:i]) + a[i:j + 1].count(0) + sum(a[j + 1:])
            if x > m:
                m = x
    return m
