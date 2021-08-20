(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
l2 = []
l4 = []
l5 = []
l6 = []
l7 = []
for i in range(m):
    l3 = input().split()
    l3[0] = int(l3[0])
    l3[1] = int(l3[1])
    l2.append(l3)
for k in range(len(l2)):
    if l2[k][0] in l:
        l4.append(k)
        l6.append(l2[k][1])
    else:
        l5.append(k)
        l7.append(l2[k][1])
while True:
    max = 0
    c = 0
    for i in range(len(l6)):
        if l6[i] > max:
            max = l6[i]
            c = i
    if max == 0:
        break
    y = int(l4[c])
    print(l2[y][2])
    l6[c] = 0
while True:
    max = 0
    c = 0
    for i in range(len(l7)):
        if l7[i] > max:
            max = l7[i]
            c = i
    if max == 0:
        break
    y = int(l5[c])
    print(l2[y][2])
    l7[c] = 0
