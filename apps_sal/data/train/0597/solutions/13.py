from sys import stdin
t = int(stdin.readline())
while t:
    n = int(stdin.readline())
    diff_prev = 0
    (d, D) = ([], [])
    h = [0]
    (x_prev, h[0]) = [int(x) for x in stdin.readline().split()]
    for i in range(n - 1):
        (x, ht) = [int(x) for x in stdin.readline().split()]
        h.append(ht)
        d.append(x - x_prev)
        D.append(diff_prev + d[i])
        diff_prev = d[i]
        x_prev = x
    D.append(d[n - 2])
    D.sort()
    h.sort()
    ans = 0
    for i in range(n):
        ans += D[i] * h[i]
    print(ans)
    t -= 1
