
x = int(input())
y = list(map(int, input().split(' ')))

y[0] = 1
y[x - 1] = 1

z = y[:]
for i in range(1, x):
    z[i] = min(z[i], z[i - 1] + 1)

w = y[:]
for i in range(x - 2, -1, -1):
    w[i] = min(w[i], w[i + 1] + 1)

ans = 0
for i in range(x):
    ans = max(ans, min(z[i], w[i]))

print(ans)
