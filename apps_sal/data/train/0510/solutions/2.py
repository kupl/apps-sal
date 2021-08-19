import sys
input = sys.stdin.readline


def segfunc(x, y):
    return x | y


def init(init_val):
    for i in range(n):
        seg[i + num - 1] = init_val[i]
    for i in range(num - 2, -1, -1):
        seg[i] = segfunc(seg[2 * i + 1], seg[2 * i + 2])


def update(k, x):
    k += num - 1
    seg[k] = x
    while k:
        k = (k - 1) // 2
        seg[k] = segfunc(seg[k * 2 + 1], seg[k * 2 + 2])


def query(p, q):
    if q <= p:
        return ide_ele
    p += num - 1
    q += num - 2
    res = ide_ele
    while q - p > 1:
        if p & 1 == 0:
            res = segfunc(res, seg[p])
        if q & 1 == 1:
            res = segfunc(res, seg[q])
            q -= 1
        p = p // 2
        q = (q - 1) // 2
    if p == q:
        res = segfunc(res, seg[p])
    else:
        res = segfunc(segfunc(res, seg[p]), seg[q])
    return res


n = int(input())
s = input()
q = int(input())
li = []
for i in range(n):
    li.append(1 << ord(s[i]) - ord('a'))
ide_ele = 0
num = 2 ** (n - 1).bit_length()
seg = [ide_ele] * 2 * num
init(li)
for _ in range(q):
    q1 = list(input().split())
    if q1[0] == '1':
        update(int(q1[1]) - 1, 1 << ord(q1[2]) - ord('a'))
    else:
        (l, r) = (int(q1[1]), int(q1[2]))
        print(bin(query(l - 1, r)).count('1'))
