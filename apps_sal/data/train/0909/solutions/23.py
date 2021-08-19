for _ in range(int(input())):
    n = int(input())
    br = list(map(int, input().split()))
    gr = list(map(int, input().split()))
    br.sort()
    gr.sort()
    flag1 = 0
    flag2 = 0
    for i in range(n - 1):
        if br[i] <= gr[i] and gr[i] <= br[i + 1]:
            cool = 1
        else:
            flag1 = 1
        if i == n - 2:
            if gr[n - 1] < br[n - 1]:
                flag1 = 1
    for i in range(n - 1):
        if gr[i] <= br[i] and br[i] <= gr[i + 1]:
            cool = 1
        else:
            flag2 = 1
        if i == n - 2:
            if br[n - 1] < gr[n - 1]:
                flag2 = 1
    if flag1 == flag2 == 1:
        print('NO')
    else:
        print('YES')
