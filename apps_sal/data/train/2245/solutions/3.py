def R():
    return list(map(int, input().split()))


def modif(lst):
    lst[0] -= 1
    lst[1] -= 1
    return lst


(n, m, k) = R()
a = R()
op = [modif(R()) for i in range(m)]
b = [0] * n
cnt = [0] * m
for i in range(k):
    (l, r) = R()
    l -= 1
    r -= 1
    cnt[l] += 1
    try:
        cnt[r + 1] -= 1
    except:
        pass
q = [0] * m
toadd = 0
for (i, v) in enumerate(cnt):
    toadd += v
    q[i] += toadd
for (i, v) in enumerate(q):
    b[op[i][0]] += op[i][2] * v
    try:
        b[op[i][1] + 1] -= op[i][2] * v
    except:
        pass
toadd = 0
for (i, v) in enumerate(b):
    toadd += v
    a[i] += toadd
print(*a)
