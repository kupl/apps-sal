t = int(input())
while t > 0:
    n, k = map(int, input().split())
    temp = {}
    for i in range(n):
        s, f, p = map(int, input().split())
        if p in temp:
            temp[p].append([s, f])
        else:
            temp[p] = [[s, f]]

    cnt = 0
    for k in temp.keys():
        temp[k].sort(key=lambda x: x[1])
        prv = [0, 0]
        for i in range(len(temp[k])):
            if temp[k][i][0] >= prv[1]:
                prv = temp[k][i]
                cnt += 1
    print(cnt)
    t -= 1
