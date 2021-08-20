(p, s) = [int(i) for i in input().split()]
l = []
for j in range(p):
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l3 = [[l1[i], l2[i]] for i in range(s)]
    l3.sort()
    count = 0
    for i in range(s - 1):
        if l3[i][1] > l3[i + 1][1]:
            count += 1
    l.append([count, j + 1])
l.sort()
for i in l:
    print(i[1])
