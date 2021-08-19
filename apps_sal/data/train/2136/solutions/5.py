(n, x, y) = (int(input()), 0, 0)
l = list(map(int, input().split()))
for a in l:
    (x, y) = (y + a // 2, x + (a + 1) // 2)
print(min(x, y))
