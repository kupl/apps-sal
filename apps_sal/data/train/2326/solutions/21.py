N = int(input())
A = list(map(int, input().split()))
num = A[0]
data = [[A[0], 0]]
for i in range(1, N):
    if A[i] > num:
        data.append([A[i], i])
        num = A[i]
B = sorted(A, reverse=True)
C = [0] * N
C[0] = B[0]
for i in range(1, N):
    C[i] = C[i - 1] + B[i]
ans = [0] * N
cnt = 0
kkk = 0
for i in range(len(data) - 1, 0, -1):
    zzz = data[i - 1][0]
    while kkk < N and B[kkk] > zzz:
        kkk += 1
    num = C[kkk - 1] - kkk * zzz
    num -= cnt
    ans[data[i][1]] = num
    cnt += num
ans[0] = sum(A) - sum(ans)
for u in ans:
    print(u)
