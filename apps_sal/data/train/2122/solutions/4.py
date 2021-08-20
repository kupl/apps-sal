t = 1
p = []
for i in range(int(input())):
    (s, d) = map(int, input().split())
    if t > s:
        for (i, q) in enumerate(p):
            if q[0] <= s <= q[0] + q[1] - d:
                print(s, s + d - 1)
                p.insert(i + 1, [s + d, q[1] - d - s + q[0]])
                q[1] = s - q[0]
                break
        else:
            for q in p:
                if q[1] >= d:
                    print(q[0], q[0] + d - 1)
                    q[0] += d
                    q[1] -= d
                    break
            else:
                print(t, t + d - 1)
                t += d
    else:
        p.append([t, s - t])
        print(s, s + d - 1)
        t = s + d
