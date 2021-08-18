a, b = map(int, input().split())
f = 0
for i in range(1, a + 1):
    for j in range(1, b + 1):
        c = i * i + j
        d = c**0.5
        e = int(d)
        if(d == e):
            f += 1
print(f)
