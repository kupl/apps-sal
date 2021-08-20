def solve(L):
    count = [0] * len(L)
    for i in range(len(L)):
        count[L[i] - 1] = i
    pL = []
    pt = len(L)
    for i in range(len(L) - 1, -1, -1):
        if pt > count[i]:
            pL.append(pt - count[i])
            pt = count[i]
    countL = [0] * 2001
    countL[0] = 1
    for i in pL:
        permL = []
        for j in range(len(countL)):
            if countL[j] and j + i < 2001:
                permL.append(i + j)
        for j in permL:
            countL[j] = 1
    return countL[len(L) // 2]


for i in ' ' * int(input()):
    n = input()
    print(['NO', 'YES'][solve(list(map(int, input().split())))])
