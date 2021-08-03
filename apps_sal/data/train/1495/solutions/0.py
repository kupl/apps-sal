t = int(input())
for i in range(0, t):
    n = int(input())
    lis = list(map(int, input().split()))
    lis2 = []
    for j in range(0, 10):
        lis2.append(0)
    for j in range(0, len(lis)):
        lis2[lis[j]] += 1
    s = sum(lis)
    while s % 3 != 0:
        if s % 3 == 2:
            if lis2[2] >= 1:
                lis2[2] -= 1
                s = s - 2
            elif lis2[5] >= 1:
                lis2[5] -= 1
                s = s - 5
            elif lis2[8] >= 1:
                lis2[8] -= 1
                s = s - 8
            elif lis2[1] >= 2:
                lis2[1] -= 2
                s = s - 2
            elif lis2[1] >= 1 and lis2[4] >= 1:
                lis2[1] -= 1
                lis2[4] -= 1
                s = s - 5
            elif lis2[4] >= 2:
                lis2[4] -= 2
                s = s - 8
            elif lis2[1] >= 1 and lis2[7] >= 1:
                lis2[1] -= 1
                lis2[7] -= 1
                s = s - 8
            elif lis2[4] >= 1 and lis2[7] >= 1:
                lis2[4] -= 1
                lis2[7] -= 1
                s = s - 11
            elif lis2[7] >= 2:
                lis2[7] -= 2
                s = s - 14
        elif s % 3 == 1:
            if lis2[1] >= 1:
                lis2[1] -= 1
                s = s - 1
            elif lis2[4] >= 1:
                lis2[4] -= 1
                s = s - 4
            elif lis2[7] >= 1:
                lis2[7] -= 1
                s = s - 7
            elif lis2[2] >= 2:
                lis2[2] -= 2
                s = s - 4
            elif lis2[5] >= 1 and lis2[2] >= 1:
                lis2[2] -= 1
                lis2[5] -= 1
                s = s - 7
            elif lis2[5] >= 2:
                lis2[5] -= 2
                s = s - 10
            elif lis2[2] >= 1 and lis2[8] >= 1:
                lis2[2] -= 1
                lis2[8] -= 1
                s = s - 10
            elif lis2[8] >= 1 and lis2[5] >= 1:
                lis2[8] -= 1
                lis2[5] -= 1
                s = s - 13
            elif lis2[8] >= 2:
                lis2[8] -= 2
                s = s - 16
    lis3 = []
    for j in range(1, 10):
        if lis2[j] >= 1:
            for k in range(0, lis2[j]):
                lis3.append(j)
    lis3.reverse()
    for k in range(0, lis2[0]):
        lis3.append(0)
    sol = ''
    for k in range(0, len(lis3)):
        sol += str(lis3[k])
    print(sol)
