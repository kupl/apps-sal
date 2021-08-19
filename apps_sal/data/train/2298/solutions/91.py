# coding: utf-8

N, T = list(map(int, input().split()))
A = [int(s) for s in input().split()]

cm = A[0]
cd = 0
cnt = 0
for i in range(1, N):
    if A[i] < cm:
        cm = A[i]
    else:
        d = A[i] - cm
        if d == cd:
            cnt += 1
        elif d > cd:
            cd = d
            cnt = 1
print(cnt)
