for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) != n or max(a) == n:
        print(-1)
        continue
    else:
        rg = []
        for i in range(n):
            if a[i] > 0:
                rg.append([i, a[i]])
        new = [0 for _ in range(n)]
        new[rg[0][0]] = rg[-1][0] + 1
        rg[-1][1] -= 1
        for i in range(1, len(rg)):
            new[rg[i][0]] = rg[i - 1][0] + 1
            rg[i - 1][1] -= 1
        j = 0
        i = 0
        while i <= n - 1:
            if new[i] == 0:
                if rg[j][1] > 0:
                    new[i] = rg[j][0] + 1
                    rg[j][1] -= 1
                    i += 1
                else:
                    j += 1
                if rg[j][1] == 0:
                    j += 1
            else:
                i += 1

        print(*new)
