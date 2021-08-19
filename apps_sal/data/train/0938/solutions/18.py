z = []
for i in range(1001):
    z.append(i * (i - 1) / 2)
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = []
    for i in range(n):
        d[a[i]].append(i)
    ans = 0
    for i in range(n):
        temp = []
        pos = []
        for j in range(i, n):
            if a[j] not in temp:
                temp.append(a[j])
                l1 = pos
                l2 = d[a[j]]
                pos = []
                i1 = 0
                i2 = 0
                len1 = len(l1)
                len2 = len(l2)
                while i1 < len1 and i2 < len2:
                    if l1[i1] < l2[i2]:
                        pos.append(l1[i1])
                        i1 += 1
                    else:
                        pos.append(l2[i2])
                        i2 += 1
                while i1 < len1:
                    pos.append(l1[i1])
                    i1 += 1
                while i2 < len2:
                    pos.append(l2[i2])
                    i2 += 1
                if pos[-1] != n - 1:
                    f = pos + [n]
                else:
                    f = pos
            curr = 0
            for p in range(1, len(f)):
                if f[p] > j:
                    xxx = f[p] - f[p - 1]
                    curr += z[xxx]
            ans += curr
    print(ans)
