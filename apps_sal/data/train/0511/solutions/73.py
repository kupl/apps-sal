N = int(input())
A = list(map(int, input().split()))
X = 0
for i in range(N):
    X = X ^ A[i]
ans = []
for i in range(N):
    temp = X ^ A[i]
    ans.append(temp)
print(*ans)
