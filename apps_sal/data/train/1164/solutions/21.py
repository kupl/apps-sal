p1, n1 = list(map(int, input().split(" ")))
x1 = list()
j = "0"
for i in range(p1):
    a1 = list(map(int, input().split(" ")))
    b1 = list(map(int, input().split(" ")))
    c = list()
    cx = 0
    al = len(a1)
    for z in range(al):
        c.append((a1[z], b1[z]))
    c = sorted(c, key=lambda x: x[0])
    ab = len(c)
    for z in range(ab - 1):
        if(c[z + 1][1] < c[z][1]):
            cx = cx + 1
    x1.append((i, cx))
x1 = sorted(x1, key=lambda x: x[1])
for i in range(len(x1)):
    print(x1[i][0] + 1)
