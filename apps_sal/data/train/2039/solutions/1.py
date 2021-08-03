N, M = list(map(int, input().split()))
A = [int(a) for a in input().split()]


def chk(k):
    ret = 0
    for i in range(N):
        a, b = A[i], (A[i] + k) % M
        if a <= b < ret:
            return 0
        if ret <= a <= b or b < ret <= a:
            ret = a
    return 1


l = -1
r = M
while r - l > 1:
    m = (l + r) // 2
    if chk(m):
        r = m
    else:
        l = m

print(r)
