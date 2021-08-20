n = int(input())
p1 = []
p2 = []
(a, b) = (0, 0)
for i in range(n):
    (s, t) = map(int, input().split(' '))
    a += s
    b += t
    if a > b:
        p1.append(a - b)
        p2.append(0)
    else:
        p2.append(b - a)
        p1.append(0)
if max(p1) > max(p2):
    print('1', max(p1), end=' ')
else:
    print('2', max(p2), end=' ')
