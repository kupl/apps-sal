for t in range(int(input())):
    l = [int(i) for i in input().split()]
    if sum(l) == 180:
        print('YES')
    else:
        print('NO')
