import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
b = a

ans = 0
for k in range(29):
    a0 = []
    a1 = []
    a0a = a0.append
    a1a = a1.append

    b0 = []
    b1 = []
    b0a = b0.append
    b1a = b1.append
    for i in a:
        if i & (1 << k):
            a1a(i)
        else:
            a0a(i)
    for i in b:
        if i & (1 << k):
            b1a(i)
        else:
            b0a(i)

    a = a0 + a1
    b = b0 + b1
    mask = (1 << (k + 1)) - 1

    aa = [i & mask for i in a]
    bb = [i & mask for i in b]

    res = 0
    p1 = 1 << k
    p2 = mask + 1
    p3 = p1 + p2

    j1 = j2 = j3 = 0
    for jj, ai in enumerate(reversed(aa)):
        while j1 < n and ai + bb[j1] < p1:
            j1 += 1
        while j2 < n and ai + bb[j2] < p2:
            j2 += 1
        while j3 < n and ai + bb[j3] < p3:
            j3 += 1
        res += max(n, n - jj) - max(j3, n - jj)
        res += max(j2, n - jj) - max(j1, n - jj)
    ans |= (res & 1) << k

print(ans)
