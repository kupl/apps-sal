n, a, b = int(input()), 0, 0
for i in map(float, input().split()):
    a, b = a + i * (1 + b * 2), i * (b + 1)
print(a)
