n = int(input())
a = []
b = []

for _ in range(n):
    ai, bi = list(map(int, input().split()))
    a.append(ai)
    b.append(bi)

s = sum(a)
mn = s
for ai, bi in zip(a, b):
    if ai <= bi:
        continue
    mn = min(bi, mn)
print((s - mn))
