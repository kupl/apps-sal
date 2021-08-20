t = int(input())
for x in range(t):
    (r, c) = map(int, input().split())
    antU = []
    antD = []
    antR = []
    antL = []
    anteater = []
    j = 0
    for y in range(r):
        s = input()
        i = 0
        for z in s:
            if z == 'U':
                antU.append([j, i, 0, i])
            elif z == 'D':
                antD.append([j, i, r - 1, i])
            elif z == 'R':
                antR.append([j, i, j, c - 1])
            elif z == 'L':
                antL.append([j, i, j, 0])
            elif z == '#':
                anteater.append([j, i])
            i = i + 1
        j = j + 1
    for y in anteater:
        for z in antU:
            if y[1] == z[1] and z[0] > y[0] and (z[2] <= y[0]):
                z[2] = y[0] + 1
        for z in antD:
            if y[1] == z[1] and z[0] < y[0] and (z[2] >= y[0]):
                z[2] = y[0] - 1
        for z in antR:
            if y[0] == z[0] and z[1] < y[1] and (z[3] >= y[1]):
                z[3] = y[1] - 1
        for z in antL:
            if y[0] == z[0] and z[1] > y[1] and (z[3] <= y[1]):
                z[3] = y[1] + 1
    total = 0
    for y in antU:
        for z in antD:
            if y[1] == z[1] and y[2] <= z[2] and (y[0] > z[0]):
                if (y[0] - z[0]) % 2 == 0:
                    total = total + 1
        for z in antR:
            if y[1] - z[1] == y[0] - z[0]:
                if y[2] <= z[0] and z[3] >= y[1]:
                    if y[0] > z[0] and y[1] > z[1]:
                        total = total + 1
        for z in antL:
            if y[1] - z[1] == z[0] - y[0]:
                if z[3] <= y[1] and y[2] <= z[0]:
                    if y[0] > z[0] and y[1] < z[1]:
                        total = total + 1
    for y in antL:
        for z in antR:
            if (y[1] - z[1]) % 2 == 0:
                if y[0] == z[0] and y[3] <= z[3] and (y[1] > z[1]):
                    total = total + 1
        for z in antD:
            if y[0] - z[0] == y[1] - z[1]:
                if y[3] <= z[1] and z[2] >= y[0]:
                    if y[0] > z[0] and y[1] > z[1]:
                        total = total + 1
    for y in antD:
        for z in antR:
            if y[0] - z[0] == z[1] - y[1]:
                if z[3] >= y[1] and y[2] >= z[0]:
                    if y[0] < z[0] and y[1] > z[1]:
                        total = total + 1
    print(total)
