(n, l, r, ql, qr) = list(map(int, input().split()))
li = list(map(int, input().split()))
ri = li.copy()
ri.append(0)
list(map(lambda x: 0, ri))
ri[0] = 0
ri[1] = li[0]
for i in range(2, len(li) + 1):
    ri[i] = ri[i - 1] + li[i - 1]
minans = 1000000000000000
s1 = 0
for j in range(0, len(li) + 1):
    if j < len(li) / 2:
        s1 = ri[j] * l + ri[len(li)] * r - ri[j] * r + qr * (len(li) - 2 * j - 1)
    elif j > len(li) / 2:
        s1 = ri[j] * l + ri[len(li)] * r - ri[j] * r + ql * (2 * j - len(li) - 1)
    else:
        s1 = ri[j] * l + ri[len(li)] * r - ri[j] * r
    minans = min([s1, minans])
print(minans)
