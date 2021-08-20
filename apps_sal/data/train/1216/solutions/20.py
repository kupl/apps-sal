t = int(input())
for i in range(t):
    (n, x) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    total = 0
    for j in a:
        if j >= x:
            total = total + 1
    if total >= 1:
        print('YES')
    else:
        print('NO')
