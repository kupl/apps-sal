N = int(input())
A = list(map(int, input().split()))
res = 0
for i in range(N):
    res ^= A[i]
ans = [a ^ res for a in A]
print(*ans)
