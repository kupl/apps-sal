t = int(input())
for _ in range(t):
    m = []
    n = int(input())
    for i in range(n):
        s = input()
        l = list(s)
        m.append(l)

    q, ans = [], []
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == "1":
                ans.append((i + 1, j + 1))
                q.append([i + 1, j + 1])

    for i in range(len(q)):
        for j in range(i + 1, len(q)):
            x, y = [0, 0], [0, 0]
            r = abs(q[i][0] - q[j][0])
            c = abs(q[i][1] - q[j][1])
            shift = abs(r - c)

            if shift == 0:
                x = min(q[i][0], q[i][1])
                y = max(q[j][0], q[j][1])
                p = ((x, x), (y, y))
            else:
                if r > c:
                    a1, a2 = min(q[i][1], q[j][1]), max(q[i][1], q[j][1])
                    if a2 + shift <= n:
                        x[1] = a1
                        y[1] = a2 + shift
                        x[0] = min(q[i][0], q[j][0])
                        y[0] = max(q[i][0], q[j][0])
                    elif a1 - shift >= 1:
                        x[1] = a1 - shift
                        y[1] = a2
                        x[0] = min(q[i][0], q[j][0])
                        y[0] = max(q[i][0], q[j][0])
                else:
                    if q[i][0] - shift >= 1:
                        x[0] = q[i][0] - shift
                        x[1] = min(q[i][1], q[j][1])
                        y[0] = q[j][0]
                        y[1] = max(q[i][1], q[j][1])
                    elif q[j][0] + shift <= n:
                        x[0] = q[i][0]
                        x[1] = min(q[i][1], q[j][1])
                        y[1] = max(q[i][1], q[j][1])
                        y[0] = q[j][0] + shift

                p = ((x[0], x[1]), (y[0], y[1]))
            ans.append(p)

    d = {}
    for i in ans:
        d[i] = 1
    print(len(d))
