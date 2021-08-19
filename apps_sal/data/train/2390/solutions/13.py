t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    P = (1 + n) * [0]
    for i in a:
        P[i] += 1
    b = []
    for i in range(1 + n):
        if P[i] != 0:
            b.append(P[i])
    b.sort()
    m = len(b) - 1
    ans = 0
    take = b[m]
    for i in range(m, -1, -1):
        if take < 0:
            break
        if 0 < b[i] <= take:
            ans += b[i]
            take = b[i] - 1
        elif b[i] > take:
            ans += take
            take -= 1
    print(ans)
    t -= 1
