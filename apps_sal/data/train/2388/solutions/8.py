import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    E = [[] for aa in range(N)]
    for __ in range(M):
        a, b = map(int, input().split())
        E[a-1].append(b-1)
        E[b-1].append(a-1)
    
    D = [-1] * N
    D[0] = 0
    d = 0
    post = [0]
    EVEN = [1]
    ODD = []
    while post:
        d += 1
        pre = post
        post = []
        for i in pre:
            for e in E[i]:
                if D[e] < 0:
                    D[e] = d
                    post.append(e)
                    if d % 2:
                        ODD.append(e+1)
                    else:
                        EVEN.append(e+1)
    if len(ODD) < len(EVEN):
        print(len(ODD))
        print(*ODD)
    else:
        print(len(EVEN))
        print(*EVEN)
