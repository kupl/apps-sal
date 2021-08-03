n = int(input())
for i in range(n):
    k, x = map(int, input().split())
    l = list(map(int, input().split()))
    f, e, o = 0, 0, 0
    for i in l:
        if(i % 2 == 0):
            e += 1
        else:
            o += 1
    if(o <= x // 2):
        f = 1
    elif(e <= x // 2):
        if((k - x) % 2 != 0):
            f = 0
        else:
            f = 1
    else:
        if(x % 2 == 0):
            f = 1
        else:
            f = 0
    if(f == 1):
        print('Jesse')
    else:
        print('Walter')
