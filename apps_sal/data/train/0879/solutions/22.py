''' PROBLEM A  '''


'''   PROBLEM B   '''


'''   PROBLEM C   '''


'''   PROBLEM D    '''


n = int(input())
for i in range(0, n):
    p = input().rstrip().split(' ')
    A = int(p[0])
    B = int(p[1])
    C = A // B
    L = []
    if C <= 10:
        M = 1
        ans = 0
        while(C):
            W = list(str(B * M))
            M += 1
            ans += int(W[len(W) - 1])
            C -= 1
        print(ans)
    else:
        M = 1
        L = []
        ans = 0
        for j in range(0, 10):
            W = list(str(B * M))
            M += 1
            L.append(int(W[len(W) - 1]))
            ans += int(W[len(W) - 1])
        D = C // 10
        E = C % 10
        tot = ans * D
        for j in range(0, E):
            tot += L[j]
        print(tot)
