import sys


def hasKey(dic, key):
    return key in list(dic.keys())


cases = int(sys.stdin.readline().rstrip())
for case in range(cases):

    [N, S] = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    p = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    t = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    costs = {}
    costs[0] = []
    costs[1] = []
    left = 100 - S
    for i in range(N):
        if t[i] == 0:
            costs[0].append(p[i])
        else:
            costs[1].append(p[i])
    error = True
    for i in costs[0]:
        for j in costs[1]:
            if (i + j <= left):
                error = False
                break
        if(error == False):
            break
    if(error):
        print("no")
    else:
        print("yes")
