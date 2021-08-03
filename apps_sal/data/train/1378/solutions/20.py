x, y, z = list(map(int, input().split()))
s = [0] * z
y = y + 1
for i in range(z):
    s[i] = x % y
    x = x // y
print(*s)
