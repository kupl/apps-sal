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
        check = [0] * (k + 1)
        (i, start, l, m, uni) = (0, 0, 0, 0, 0)
        while i < len(t) and start < len(t):
            check[t[i]] += 1
            if check[t[i]] == 1:
                uni += 1
            if uni == k:
                check[t[i]] -= 1
                m = max(m, l)
                check[t[start]] -= 1
                if check[t[start]] == 0:
                    uni -= 1
                l -= f[start]
                start += 1
                uni -= 1
                continue
            l += f[i]
            i += 1
        m = max(m, l)
        print(m)
