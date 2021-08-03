N = int(input())
a = list(map(int, input().split()))
ans = []
x = a[0]
for i in range(1, N):
    x ^= a[i]
for i in a:
    ans.append(x ^ i)
print(*ans)
