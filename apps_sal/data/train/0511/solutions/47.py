n = int(input())
a = list(map(int, input().split()))

b = 0
for i in range(n):
    b ^= a[i]
x = []
for i in range(n):
    x.append(b ^ a[i])
print(*x)
