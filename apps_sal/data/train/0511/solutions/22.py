n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(n):
    s = s ^ a[i]
ans = []
for j in range(n):
    tmp = s ^ a[j]
    ans.append(tmp)
print(*ans)
