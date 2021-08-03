for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    flag = 1
    for i in range(n - 1):
        for j in range(n - 1):
            if(a[i][j] == 1):
                if(a[i + 1][j] == 1 or a[i][j + 1] == 1):
                    flag = 0
                    break
                else:
                    pass
    j = 0
    i = n - 1
    while(j < n - 1):
        if(a[i][j] == 1):
            if(a[i][j + 1] == 1):
                flag = 0
                break
            else:
                pass
        j += 1
    i = 0
    j = n - 1
    while(i < n - 1):
        if(a[i][j] == 1):
            if(a[i + 1][j] == 1):
                flag = 0
                break
            else:
                pass
        i += 1
    if(flag == 1):
        print('SAFE')
    else:
        print('UNSAFE')
