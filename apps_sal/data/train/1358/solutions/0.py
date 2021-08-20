import bisect
for _ in range(int(input())):
    (w, k) = map(str, input().split())
    k = int(k)
    n = len(w)
    w = list(w)
    w.sort()
    w.append('0')
    c = 1
    l = 0
    l1 = []
    l2 = []
    for i in range(1, n + 1):
        if w[i] == w[i - 1]:
            c += 1
        else:
            a = bisect.bisect_left(l1, c)
            if a == l:
                l1.append(c)
                l2.append(1)
                l += 1
            elif l1[a] == c:
                l2[a] = l2[a] + 1
            else:
                l1.insert(a, c)
                l2.insert(a, 1)
                l += 1
            c = 1
    a = l1[-1] - l1[0]
    if a <= k:
        print(0)
    else:
        ans = n
        for i in range(l):
            temp = l2[i] * l1[i]
            for j in range(i + 1, l):
                p = l1[j] - l1[i]
                if p <= k:
                    temp += l2[j] * l1[j]
                else:
                    p1 = p - k
                    temp += l2[j] * (l1[j] - p1)
            ans = min(ans, n - temp)
        print(ans)
