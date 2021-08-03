n, m = map(int, input().split())
out, inp = [0] * (n + 1), [0] * (n + 1)
inset = [[] for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())

    if x > y:
        z = x
        x = y
        y = z

    out[y] += 1
    inp[x] += 1
    inset[x].append(y)

q = int(input())

res = 0
for ind in range(1, n + 1):
    res += inp[ind] * out[ind]

print(res)
for i in range(q):
    best = int(input())

    res -= out[best] * inp[best]
    for pred_ind in inset[best]:
        res += -out[pred_ind] * inp[pred_ind] + ((out[pred_ind] - 1) * (inp[pred_ind] + 1))
        out[pred_ind] -= 1
        inp[pred_ind] += 1
        inset[pred_ind].append(best)

    out[best] += inp[best]
    inp[best] = 0
    inset[best] = []

    print(res)
