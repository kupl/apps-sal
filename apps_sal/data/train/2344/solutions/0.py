import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    X = [[] for i in range(3*N)]
    for i in range(M):
        x, y = list(map(int, input().split()))
        x, y = min(x,y), max(x,y)
        X[x-1].append((y-1, i+1))
    
    MAT = []
    IND = []
    DONE = [0] * 3*N
    for i in range(3*N):
        if DONE[i]: continue
        for j, ind in X[i]:
            if DONE[j] == 0:
                MAT.append(ind)
                DONE[i] = 1
                DONE[j] = 1
                break
        else:
            IND.append(i+1)

    if len(MAT) >= N:
        print("Matching")
        print(*MAT[:N])
    else:
        print("IndSet")
        print(*IND[:N])



