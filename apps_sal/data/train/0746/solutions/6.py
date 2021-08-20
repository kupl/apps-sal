import sys
f = sys.stdin
while True:
    H = int(f.readline())
    if H == 0:
        break
    v = list(map(int, f.readline().split()))
    p = [0] * 2 ** H
    for i in range(2 ** H - 1, 0, -1):
        if i * 2 >= 2 ** H:
            p[i] = v[i - 1]
        else:
            p[i] = v[i - 1] * max(p[2 * i], p[2 * i + 1])
    r = p[1] % 1000000007
    print(r)
