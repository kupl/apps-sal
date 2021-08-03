def flipping_game(num):
    if 0 not in num:
        return len(num) - 1
    elif num == [0]:
        return 1
    m = -1
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num) + 1):
            c = num[:i].count(1) + num[i:j].count(0) + num[j:].count(1)
            if c > m:
                m = c
    return m
