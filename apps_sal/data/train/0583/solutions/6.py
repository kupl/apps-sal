for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    k = sum(b)
    if k >= 0:
        print('YES')
    else:
        print('NO')
