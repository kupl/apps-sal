t = int(input())
for _ in range(t):
    (n, k, e, m) = [int(x) for x in input().split()]
    s = []
    for i in range(n - 1):
        a = [int(x) for x in input().split()]
        s.append(sum(a))
    s.sort()
    s.reverse()
    a = [int(x) for x in input().split()]
    ap = sum(a)
    ans = s[k - 1] + 1 - sum(a)
    if ans > m:
        print('Impossible')
    elif ans > 0:
        print(ans)
    else:
        print(0)
