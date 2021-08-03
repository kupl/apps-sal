
n = int(input())
c = 0
f = 0
m = 10000000000000000000000
for i in range(n):
    a, b = list(map(int, input().split()))
    c += a
    if a > b:
        m = min(b, m)
    if a != b:
        f = 1
print(((c - m) * f))
