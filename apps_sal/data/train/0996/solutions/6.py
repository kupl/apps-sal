# cook your dish here
l = 0
m = 0
p1 = [0]
p2 = [0]
l1 = [0]
l2 = [0]
for i in range(int(input())):
    a, b = map(int, input().split())
    p1.append(a + l)
    p2.append(b + m)
    l = p1[-1]
    m = p2[-1]
for x, y in zip(p1, p2):
    d = x - y
    if(d > 0):
        l1.append(d)
    if(d < 0):
        l2.append(abs(d))
if(max(l1) > max(l2)):
    print(1, end=" ")
    print(max(l1))
else:
    print(2, end=" ")
    print(max(l2))
