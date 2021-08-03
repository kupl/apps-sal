p = str(input())
s = []
e = []
ip = []
for i in range(int(input())):
    temp = str(input())
    ip.append(temp)
    s.append(temp[0])
    e.append(temp[1])
b = 0
if p in ip:
    b = 1
else:
    if p[0] in e and p[1] in s:
        b = 1
if b == 1:
    print('YES')
else:
    print('NO')
