p = input().strip()
r = []
for i in range(len(p)):
    s = int(p[i])
    k = 0
    for j in range(i, len(p) - 1):
        if p[j + 1] > p[j]:
            s = s + int(p[j + 1])
            k += 1
        else:
            break
    r.append([i + 1, i + k + 1, s])
for i in range(len(r)):
    for j in range(i + 1, len(r)):
        if r[i][2] > r[j][2]:
            c = r[j]
            r[j] = r[i]
            r[i] = c
print('{}:{}-{}'.format(r[-1][2], r[-1][0], r[-1][1]))
