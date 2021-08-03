import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(29):
    div_ = pow(2, i + 1)
    A_tmp = sorted([x % div_ for x in A])
    B_tmp = sorted([x % div_ for x in B])
    cnt = 0
    tmp = pow(2, i)
    idx1 = N
    idx2 = N
    idx3 = N
    for a in A_tmp:
        idx2 = bisect.bisect_left(B_tmp, 2 * tmp - a, hi=idx2)
        idx1 = bisect.bisect_left(B_tmp, tmp - a, hi=min(idx1, idx2))
        idx3 = bisect.bisect_left(B_tmp, 3 * tmp - a, lo=idx2, hi=idx3)
        cnt += ((idx2 - idx1) + (N - idx3)) % 2
    if cnt % 2 == 1:
        ans += tmp
print(ans)
