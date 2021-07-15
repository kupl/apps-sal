import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    ''' inputs '''
    n = int(sys.stdin.readline())                         # single input
    # n, m = map(int, sys.stdin.readline().split())         # two inputs
    # A = list(map(int, sys.stdin.readline().split()))      # list input
    '''code here'''
    M = []
    for i in range(n):
        M.append(list(map(int, list(sys.stdin.readline().strip()))))
        
    res = True
    
    for i in range(n-1):
        for j in range(n-1):
            if M[i][j] == 1 and M[i+1][j] == 0 and M[i][j+1] == 0:
                res = False
                break
    
    print("YES" if res else "NO")

