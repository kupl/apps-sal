n = int(input())
arr = list(map(int, input().split()))
a = 0
for i in range(n):
    a ^= arr[i]
ans = []
for i in range(n):
    ans.append(a ^ arr[i])
print(*ans)
