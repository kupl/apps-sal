t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    m = list(map(int, input().split()))
    a = 0
    for i in m:
        if i >= k:
            a = 1
            break
    if a == 1:
        print('YES')
    else:
        print('NO')
