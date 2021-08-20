n = int(input())
a = list(map(int, input().split()))
s = a[0]
for i in range(1, n):
    s ^= a[i]
ans = [0] * n
for j in range(n):
    ans[j] = s ^ a[j]
print(*ans)
