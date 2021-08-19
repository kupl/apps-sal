def comfortable_numbers(l, r):
    ct = 0
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            it = sum((int(c) for c in str(i)))
            jt = sum((int(c) for c in str(j)))
            if i - jt <= j <= i + jt and j - it <= i <= j + it:
                ct += 1
    return ct
