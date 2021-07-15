import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(29):
    div_ = pow(2, i+1)
    A_tmp = sorted([x%div_ for x in A])
    B_tmp = sorted([x%div_ for x in B])
    cnt = 0
    tmp = pow(2, i)
    idx1 = N
    idx2 = N
    idx3 = N
    for a in A_tmp:
        while idx2>0 and B_tmp[idx2-1]>=2*tmp-a:
            idx2 -= 1
        while idx1>0 and B_tmp[idx1-1]>=tmp-a:
            idx1 -= 1
        while idx3>0 and B_tmp[idx3-1]>=3*tmp-a:
            idx3 -= 1
        cnt += ((idx2-idx1)+(N-idx3))%2
    if cnt % 2 == 1:
        ans += tmp
print(ans)

