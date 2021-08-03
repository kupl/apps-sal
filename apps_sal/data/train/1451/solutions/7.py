for _ in range(int(input())):
    l = []
    mp = {}
    cr = {}
    ans = []
    n, m = map(int, input().split())
    for i in range(1, n + 1):
        mp[i] = 0
        cr[i] = False
    for _ in range(m):
        f, t = map(int, input().split())
        l.append((f, t))
        mp[f] += 1
        mp[t] += 1
    if m % 2 > 0:
        print(-1)
        continue
    else:
        for _ in range(m):
            cr[l[_][1]] = not cr[l[_][1]]
            ans.append(0)
        for _ in range(m - 1, -1, -1):
            if cr[l[_][1]] == True:
                cr[l[_][1]] = not True
                ans[_] = 1
                if cr[l[_][0]]:
                    cr[l[_][0]] = False
                else:
                    cr[l[_][0]] = True
        for i in range(len(ans)):
            print(ans[i], end=' ')
        print()
