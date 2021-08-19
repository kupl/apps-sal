for i in range(int(input())):
    (n, x) = map(int, input().split(' '))
    l = list(map(int, input().split(' ')))
    for j in range(len(l)):
        if l[j] >= x:
            print('YES')
            break
    else:
        print('NO')
