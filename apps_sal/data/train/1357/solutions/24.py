import sys


def hasKey(dic, key):
    return key in dic.keys()


cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    N = int(sys.stdin.readline().rstrip())
    p = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    change = 0
    error = False
    for pi in p:
        if pi - 5 <= change:
            change = change - (pi - 5)
            change += 5
        else:
            error = True
            break
    if error:
        print('NO')
    else:
        print('YES')
