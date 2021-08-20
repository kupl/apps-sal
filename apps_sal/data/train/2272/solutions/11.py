from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
T = 1 << 30
for k in range(30, -1, -1):
    cnt = 0
    TT = T << 1
    for i in range(N):
        A[i] %= TT
        B[i] %= TT
    A = sorted(A)
    B = sorted(B)
    d0 = bisect_left(B, T - A[0])
    d1 = bisect_left(B, 2 * T - A[0])
    d2 = bisect_left(B, 3 * T - A[0])
    for i in range(N):
        while d0 - 1 >= 0 and B[d0 - 1] >= T - A[i]:
            d0 -= 1
        while d1 - 1 >= 0 and B[d1 - 1] >= 2 * T - A[i]:
            d1 -= 1
        while d2 - 1 >= 0 and B[d2 - 1] >= 3 * T - A[i]:
            d2 -= 1
        cnt += d1 - d0
        cnt += N - d2
    if cnt % 2 == 1:
        ans |= T
    T = T >> 1
print(ans)
