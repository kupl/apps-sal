# cook your dish here
d, x, y = map(int, input().split())
l = list(map(int, input().split()))
s = 0
s += d * x
tip = y
tipm = 0
n = len(l)
for i in range(n):
    y = tip
    for j in range(6 * (l[i] - 1)):
        y -= 0.02 * y
    tipm += y
s += tipm
# print(s)
if s >= 300:
    print('YES')
else:
    print('NO')
