import collections
for _ in range(1):
    (n, p) = list(map(int, input().split()))
    a = sorted(map(int, input().split()))
    c = s = 0
    for v in a:
        if s + v > p:
            break
        s += v
        c += 1
    print(c)
