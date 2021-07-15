t = int(input())
for i in range(t):
    q = input().split()
    n = int(q[0])
    m = int(q[1])
    k = int(q[2])
    sumax = 0
    b = []
    for j in range(n):
        a = [int(k) for k in input().split()]
        b = b + [a]
    for j in range(n):
        su = 0
        for x in range(k):
            su = su +b[j][x]
            if su > sumax:
                sumax = su
        for a in range(1, m-k+1):
            su = su - b[j][a-1] +b[j][k+a-1]
            if su > sumax:
                sumax = su
    for j in range(m):
        su = 0
        for x in range(k):
            su = su + b[x][j]
            if su > sumax:
                sumax = su
        for a in range(1, n-k+1):
            su = su - b[a-1][j] + b[a+k-1][j]
            if su > sumax:
                sumax = su
    print(sumax)
            
    

