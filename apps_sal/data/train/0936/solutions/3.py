t = int(input())
while(t > 0):
    t -= 1
    aa = int(input())
    count = 0
    blist = []
    for i in range(aa):
        blist.append([int(x) for x in input().split()])
    for d in range(aa - 1, 0, -1):
        result = blist[d][d - 1] + 1
        if result != blist[d][d]:
            count += 1
            next = d + 1
            for i in range(next):
                for j in range(i, next):
                    temp = blist[i][j]
                    blist[i][j] = blist[j][i]
                    blist[j][i] = temp
    print(count)
