T = int(input())
for i in range(0, T):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = 0
    for x in arr:
        if x < 0:
            flag = 1
            break
    if flag == 1:
        print('NO')
    else:
        print('YES')
