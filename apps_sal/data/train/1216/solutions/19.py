for _ in range(int(input())):
    (n, X) = map(int, input().split(' '))
    l = list(map(int, input().split(' ')))
    count = 0
    flag = 0
    for x in l:
        if x >= X:
            flag = 1
            print('YES')
            break
    if flag == 0:
        print('NO')
