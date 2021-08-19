N = int(input())
A = [int(a) for a in input().split()]
ans = [0] * N
num = 0
B = sorted(A)
j = 0
for i in range(N):
    cnt = 0
    while j < N and B[j] <= A[i]:
        cnt += max(0, B[j] - num)
        j += 1
    ans[i] = cnt + max(0, (N - j) * (A[i] - num))
    num = max(num, A[i])
for a in ans:
    print(a)
