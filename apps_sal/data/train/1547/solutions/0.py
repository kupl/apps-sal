try:
    d1, v1, d2, v2, p = map(int, input().split())
    total = 0
    while p > 0:
        total += 1
        if total >= d1:
            p = p - v1
        if total >= d2:
            p = p - v2
    print(total)
except:
    pass
