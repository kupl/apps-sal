import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    ''' inputs '''
    n = int(sys.stdin.readline())
    '''code here'''
    M = []
    for i in range(n):
        M.append(list(map(int, list(sys.stdin.readline().strip()))))

    res = True

    for i in range(n - 1):
        for j in range(n - 1):
            if M[i][j] == 1 and M[i + 1][j] == 0 and M[i][j + 1] == 0:
                res = False
                break

    print("YES" if res else "NO")
