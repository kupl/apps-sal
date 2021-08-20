n = int(input())
s = []
for i in range(n):
    (a, b, c, d) = list(map(int, input().split()))
    s.append((-(a + b + c + d), i))
    if i == 0:
        x = -(a + b + c + d)
s.sort()
print(1 + s.index((x, 0)))
