t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    search = 0
    for i in range(len(a)):
        if a[i] < 0:
            search = 1
            break
    if search == 1:
        print('NO')
    else:
        print('YES')
