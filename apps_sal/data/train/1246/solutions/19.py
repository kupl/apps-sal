for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if max(a) - max(b) == 0:
        print('NO')
    else:
        print('YES')
