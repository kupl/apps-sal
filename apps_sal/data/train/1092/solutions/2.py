t = int(input())
for i in range(t):
    (n, k, e, m) = map(int, input().split())
    p = []
    for i in range(n - 1):
        p.append(sum(map(int, input().split())))
    q = sum(map(int, input().split()))
    p.sort()
    d = p[n - k - 1] - q
    if d + 1 > m:
        print('Impossible')
    elif d <= -1:
        print(0)
    else:
        print(d + 1)
