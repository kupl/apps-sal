for i in range(int(input())):
    (h, x) = [int(x) for x in input().split()]
    if h >= x:
        print('Yes')
    else:
        print('No')
