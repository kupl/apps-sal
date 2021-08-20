try:
    (a, b, c) = list(map(int, input().split()))
    r = 0
    for _ in range(c):
        (w, x, y, z) = list(map(int, input().split()))
        r += abs(w - y)
        r += 2 * abs(x - z)
    print(r)
except:
    pass
