for u in range(int(input())):
    n, m = list(map(int, input().split()))
    c = 0
    if(m < 9):
        print(0, 0)
    else:
        for i in str(m):
            if(i == '9'):
                c += 1
        if(c == len(str(m))):
            print(n * c, n)
        else:
            x = len(str(m)) - 1
            print(x * n, n)
