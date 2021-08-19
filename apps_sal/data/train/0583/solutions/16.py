T = int(input())
for i in range(0, T):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = 0
    if sum(arr) < 0:
        flag = 1
    if flag == 1:
        print('NO')
    else:
        print('YES')
