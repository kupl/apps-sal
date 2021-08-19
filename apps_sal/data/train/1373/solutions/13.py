for T in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if len(set(a)) < k:
        print(len(a))
    else:
        (f, t, c) = ([], [], 1)
        key = a[0]
        for i in range(1, n):
            if a[i] == key:
                c += 1
            else:
                f.append(c)
                t.append(key)
                key = a[i]
                c = 1
        f.append(c)
        t.append(key)
        (check, uni, start, i) = ([], 0, 0, 0)
        (l, m) = (0, 0)
        while i < len(t) and start < len(t):
            if t[i] not in check:
                uni += 1
            if uni == k:
                m = max(m, l)
                check.remove(t[start])
                if t[start] not in check:
                    uni -= 1
                uni -= 1
                l -= f[start]
                start += 1
                continue
            check.append(t[i])
            l += f[i]
            i += 1
        m = max(m, l)
        print(m)
