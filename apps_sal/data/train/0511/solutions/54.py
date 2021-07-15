n = int(input())
lis = list(map(int, input().split()))

t = lis[0]
for i in range(1, n):
    t ^= lis[i]

ans = [0] * n
for i , j in enumerate(lis):
    ans[i] = t ^ j

print(*ans)
