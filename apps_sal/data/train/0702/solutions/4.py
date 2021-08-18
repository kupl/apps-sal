for _ in range(int(input())):
    m, t1, t2 = map(int, input().split())
    d = max(t1, t2) - min(t1, t2)
    if(d % 3 != 0):
        print('Yes')
    else:
        if(d // 3 > m):
            print('Yes')
        else:
            print('No')
