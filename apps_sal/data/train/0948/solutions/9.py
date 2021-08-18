a, b = map(int, input().split())
c = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        x = i * i + j
        d = x**0.5
        e = int(d)
        if d == e:
            c += 1
print(c)
