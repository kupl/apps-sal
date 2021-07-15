try:
    N, M = list(map(int, input().split()))
    L = []
    for i in range(N+M):
        a = int(input())
        if a != -1:
            L.append(a)
        else:
            print(max(L))
            L.remove(max(L))
except:
    pass
    

