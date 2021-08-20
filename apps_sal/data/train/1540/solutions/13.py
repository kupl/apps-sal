t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    if k < n:
        print('NO')
    elif k % n == 0:
        print('YES')
    else:
        print('NO')
