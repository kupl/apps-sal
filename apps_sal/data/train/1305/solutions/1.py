T = int(input())
for t in range(T):
    N = int(input())
    l = []
    for i in range(N):
        l.append(list(map(int, input().split())))
    flg = True
    for i in range(N):
        for j in range(1, N):
            if l[i][j] == l[i][j - 1] and l[i][j] == 1:
                flg = False
                break
        if flg == False:
            break
    if flg == False:
        print('UNSAFE')
    else:
        for i in range(1, N):
            for j in range(N):
                if l[i][j] == l[i - 1][j] and l[i][j] == 1:
                    flg = False
                    break
            if flg == False:
                break
        if flg == False:
            print('UNSAFE')
        else:
            print('SAFE')
