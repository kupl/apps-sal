n = int(input())
b = int(n ** 0.5)
ans = []
for i in range(0, n, b):
    ans = [j for j in range(i + 1, min(i + 1 + b, n + 1))] + ans
print(*ans)
