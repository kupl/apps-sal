t, p = 1, []
for i in range(int(input())):
    l, d = map(int, input().split())
    if t > l:
        for i, q in enumerate(p, 1):
            if q[0] <= l <= q[1] - d:
                p.insert(i, [l + d, q[1]])
                q[1] = l
                break
        else:
            for q in p:
                if q[0] <= q[1] - d:
                    l = q[0]
                    q[0] += d
                    break
            else:
                l = t
                t += d
    else:
        p.append([t, l])
        t = l + d

    print(l, l + d - 1)
