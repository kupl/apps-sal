try:
    t = int(input())
    while t > 0:
        (n, q) = map(int, input().split())
        A = [j for j in input().split()]
        tmp = []
        while q > 0:
            tmp += [j for j in input().split()]
            q -= 1
        i = 0
        while n > i:
            if A[i] in tmp:
                print('YES', end=' ')
            else:
                print('NO', end=' ')
            i += 1
        print()
        t -= 1
except:
    pass
