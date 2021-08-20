def bitadd(a, w, bit):
    x = a
    while x <= len(bit) - 1:
        bit[x] += w
        x += x & -1 * x


def bitsum(x, bit):
    ret = 0
    while x:
        ret += bit[x]
        x -= x & -1 * x
    return ret


def bitaddR(l, r, w, bit1, bit2):
    bitadd(l, -1 * w * l, bit1)
    bitadd(r, w * r, bit1)
    bitadd(l, w, bit2)
    bitadd(r, -1 * w, bit2)


def bitsumR(r, bit1, bit2):
    return bitsum(r, bit1) + r * bitsum(r, bit2)


(N, M) = list(map(int, input().split()))
BIT = [0] * (M + 1)
dic = {}
for i in range(N):
    (l, r) = list(map(int, input().split()))
    if r - l + 1 not in dic:
        dic[r - l + 1] = []
    dic[r - l + 1].append([l, r])
ind = 0
ns = N
ans = []
for d in range(M):
    d += 1
    if d in dic:
        for (L, R) in dic[d]:
            bitadd(L, 1, BIT)
            bitadd(R + 1, -1, BIT)
            ns -= 1
    nm = 0
    for i in range(d, M + 1, d):
        nm += bitsum(i, BIT)
    ans.append(nm + ns)
print('\n'.join(map(str, ans)))
