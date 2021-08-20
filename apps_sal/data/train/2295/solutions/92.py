n = int(input())
s = 0
f = False
m = 10 ** 9
for i in range(n):
    (a, b) = map(int, input().split())
    s += a
    if a < b:
        f = True
    if a > b:
        f = True
        m = min(m, b)
if f:
    print(s - m)
else:
    print(0)
