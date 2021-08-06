t = int(input())
l = []
l1 = []
p1 = 0
p2 = 0
for i in range(t):
    n, m = map(int, input().split())
    p1 += n
    p2 += m
    if p1 > p2:
        l.append(p1 - p2)
        l1.append(0)
    else:
        l.append(0)
        l1.append(p2 - p1)
m1 = max(l)
m2 = max(l1)
if m1 > m2:
    print(1, m1)
else:
    print(2, m2)
