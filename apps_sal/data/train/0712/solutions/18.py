for i in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    flag = 0
    for j in b:
        if j % 2 == 0:
            flag += 1
            break
    if flag == 0:
        print('YES')
    else:
        print('NO')
