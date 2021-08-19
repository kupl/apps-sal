from sys import stdin
c = int(stdin.readline().strip())
for cas in range(c):
    n = int(stdin.readline().strip())
    s = [list(map(int, stdin.readline().strip().split())) for i in range(n)]
    mn = -10 ** 5
    interval = [[mn, -mn], [mn, -mn]]
    flag = True
    for i in s:
        if i[2] == 0:
            if interval[0][1] < i[0]:
                flag = False
                break
            else:
                interval[0][0] = max(i[0], interval[0][0])
        if i[3] == 0:
            if interval[1][0] > i[1]:
                flag = False
                break
            else:
                interval[1][1] = min(interval[1][1], i[1])
        if i[4] == 0:
            if interval[0][0] > i[0]:
                flag = False
                break
            else:
                interval[0][1] = min(interval[0][1], i[0])
        if i[5] == 0:
            if interval[1][1] < i[1]:
                flag = False
                break
            else:
                interval[1][0] = max(interval[1][0], i[1])
    if flag:
        print(1, interval[0][0], interval[1][0])
    else:
        print(0)
