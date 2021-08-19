straight = set([1, 2])
nstraight = set([3, 4, 5, 6])
for _ in range(int(input())):
    n = int(input())
    r1 = [int(x) for x in input().strip()]
    r2 = [int(x) for x in input().strip()]
    poss = [True, False]
    for i in range(n):
        possnew = [False, False]
        if poss[0] and r1[i] in straight:
            possnew[0] = True
        if poss[1] and r2[i] in straight:
            possnew[1] = True
        if r1[i] in nstraight and r2[i] in nstraight:
            if poss[0]:
                possnew[1] = True
            if poss[1]:
                possnew[0] = True
        poss = possnew
    if poss[1]:
        print('YES')
    else:
        print('NO')
