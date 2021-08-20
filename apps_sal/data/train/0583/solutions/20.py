for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if sum(arr) < 0:
        print('NO')
    else:
        print('YES')
