for _ in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))
    d = {i: [] for i in range(1, 27)}
    for i in range(n):
        d[r[i]].append(i)
    ans = 1
    for end in range(1, 27):
        c = 1
        while c * 2 <= len(d[end]):
            (ll, rr) = (d[end][c - 1] + 1, d[end][-c] - 1)
            dd = [0] * 27
            for p in range(ll, rr + 1):
                dd[r[p]] += 1
            ans = max(ans, max(dd) + 2 * c)
            c += 1
    print(ans)
