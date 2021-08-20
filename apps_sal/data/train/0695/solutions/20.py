t = int(input())
for _ in range(t):
    (x, y, n) = list(map(int, input().split()))
    ct = 0
    for z in range(n + 1):
        if z ^ x < z ^ y:
            ct += 1
    print(ct)
