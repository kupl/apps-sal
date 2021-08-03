n, k = list(map(int, input().split()))
m = []
c = 0
for i in range(4):
    m.append(list(map(int, input().split())))
res = []
for i in range(n):
    if m[1][i] != 0:
        if m[1][i] == m[0][i]:
            res.append([m[1][i], 1, i + 1])
            m[1][i] = 0
            k -= 1
for i in range(n):
    if m[2][i] != 0:
        if m[2][i] == m[3][i]:
            res.append([m[2][i], 4, i + 1])
            m[2][i] = 0
            k -= 1
if k >= n * 2:
    print(-1)
    return
if True:
    while True:
        c += 1
        for i in range(n):
            if m[1][i] != 0:
                if i != 0:
                    if m[1][i - 1] == 0:
                        res.append([m[1][i], 2, i])
                        m[1][i - 1] = m[1][i]
                        m[1][i] = 0
                        if m[0][i - 1] == m[1][i - 1]:
                            res.append([m[1][i - 1], 1, i])
                            m[0][i - 1] = m[1][i - 1]
                            m[1][i - 1] = 0
                            k -= 1
                elif i == 0:
                    if m[2][i] == 0:
                        res.append([m[1][i], 3, i + 1])
                        m[2][i] = m[1][i]
                        m[1][i] = 0
                        if m[3][i] == m[2][i]:
                            res.append([m[2][i], 4, i + 1])
                            m[3][i] = m[2][i]
                            m[2][i] = 0
                            k -= 1
        for i in range(n):
            if m[2][i] != 0:
                if i != n - 1:
                    if m[2][i + 1] == 0:
                        res.append([m[2][i], 3, i + 2])
                        m[2][i + 1] = m[2][i]
                        m[2][i] = 0
                        if m[3][i + 1] == m[2][i + 1]:
                            res.append([m[2][i + 1], 4, i + 2])
                            m[3][i + 1] = m[2][i + 1]
                            m[2][i + 1] = 0
                            k -= 1
                else:
                    if m[1][i] == 0:
                        res.append([m[2][i], 2, i + 1])
                        m[1][i] = m[2][i]
                        m[2][i] = 0
                        if m[0][i] == m[1][i]:
                            res.append([m[1][i], 1, i + 1])
                            m[0][i] = m[1][i]
                            m[1][i] = 0
                            k -= 1
        if k <= 0:
            break

else:
    print(-1)
    return
print(len(res))
for i in res:
    print(*i)
