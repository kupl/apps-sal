t = int(input())
for z in range(0, t):
    N = int(input())
    li = [[i for i in range(0, N)] for j in range(0, N)]
    c = 1
    for j1 in range(0, N):
        i = 0
        j = j1
        while j != -1:
            li[i][j] = c
            i += 1
            j -= 1
            c += 1
    for i1 in range(1, N):
        j = N - 1
        i = i1
        while i != N:
            li[i][j] = c
            i += 1
            j -= 1
            c += 1
    for i in range(0, N):
        for j in range(0, N):
            print(li[i][j], end=' ')
        print()
