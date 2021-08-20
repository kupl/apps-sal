(n, u) = input().split()
a = input().split()
x = dict()
t = list()
v = list()
for i in range(int(u)):
    b = input().split()
    x[int(b[1])] = [b[0], b[2]]
for i in list(x.items()):
    if i[1][0] in a:
        v.append(i[1][1])
    else:
        t.append(i[1][1])
for i in v[::-1]:
    print(i)
for i in t[::-1]:
    print(i)
