import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))
A.sort()
B.sort()
cnta = [0] * 29
cntb = [0] * 29
for idx in range(N):
    (a, b) = (A[idx], B[idx])
    for i in range(29):
        if 1 << i & a:
            cnta[i] = 1 - cnta[i]
        if 1 << i & b:
            cntb[i] = 1 - cntb[i]
carry = [0] * 30
bwa = [0] * N
bwb = [0] * N
for i in range(29):
    m = (1 << i + 1) - 1
    bwbc = sorted([b & m for b in B])
    bwac = sorted([m + 1 if a & m == 0 else m & -(a & m) for a in A])
    r = N
    for idx in range(N - 1, -1, -1):
        a = bwac[idx]
        while r and bwbc[r - 1] >= a:
            r -= 1
        carry[i + 1] += N - r
ans = 0
for i in range(29):
    if (carry[i] + (cnta[i] + cntb[i]) * N) % 2 == 1:
        ans |= 1 << i
print(ans)
