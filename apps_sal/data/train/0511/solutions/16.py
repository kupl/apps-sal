n = int(input())
A = list(map(int, input().split()))
aa = 0
for i in A:
    aa ^= i
ans = [0] * n
for i in range(n):
    ans[i] = aa ^ A[i]
print(' '.join(map(str, ans)))
