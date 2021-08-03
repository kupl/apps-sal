q = int(input())
for i in range(q):
    a, b = list(map(int, input().split()))
    p = int((a * b - 1)**0.5)
    if p * p > a * b - 1:
        p = p - 1
    r = p * 2 - 1
    if p * p + p > a * b - 1:
        r = r - 1
    if a == b:
        r = r + 1
    print(r)
