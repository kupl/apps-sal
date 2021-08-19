import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().strip()))


def calc(l, r):
    m = (l + r) // 2
    if l + 1 == r:
        return A[l]
    if l + 2 == r:
        return 2 * (A[l] + A[l + 1])
    X = A[l:m][::-1]
    Y = A[m:r]
    LX = len(X)
    LY = len(Y)
    a1 = [0] * LX
    a2 = [0] * LY
    pre = 1
    cnt = 0
    b1 = 0
    b2 = 0
    for i in range(LX):
        if X[i]:
            cnt += 1
            if pre:
                a1[i] = cnt
                b1 = cnt
            else:
                a1[i] = max(a1[i - 1], cnt)
        else:
            pre = 0
            cnt = 0
            a1[i] = a1[i - 1]
    pre = 1
    cnt = 0
    for i in range(LY):
        if Y[i]:
            cnt += 1
            if pre:
                a2[i] = cnt
                b2 = cnt
            else:
                a2[i] = max(a2[i - 1], cnt)
        else:
            pre = 0
            cnt = 0
            a2[i] = a2[i - 1]
    ra = LX - 1
    rb = LY - 1
    i = ra
    j = rb
    res = 0
    for _ in range(LX + LY):
        if a1[i] >= a2[j]:
            a = a1[i]
            if b1 + b2 <= a:
                res += a * (j + 1)
            elif a == b1:
                res += b1 * b2 + b2 * (b2 + 1) // 2 + (b1 + b2) * (j + 1 - b2)
            else:
                res += a * b2 + (b1 + b2 - a) * (b1 + b2 - a + 1) // 2 + (b1 + b2) * (j + 1 - b2)
            i -= 1
            b1 = min(b1, i + 1)
        else:
            a = a2[j]
            if b1 + b2 <= a:
                res += a * (i + 1)
            elif a == b2:
                res += b1 * b2 + b1 * (b1 + 1) // 2 + (b1 + b2) * (i + 1 - b1)
            else:
                res += a * b1 + (b1 + b2 - a) * (b1 + b2 - a + 1) // 2 + (b1 + b2) * (i + 1 - b1)
            j -= 1
            b2 = min(b2, j + 1)
        if i == -1 or j == -1:
            break
    return res + calc(l, m) + calc(m, r)


print(calc(0, N))
