for t in range(int(input())):
    (n, x) = map(int, input().split())
    arr = list(map(int, input().split()))
    if max(arr) - min(arr) < x:
        print('YES')
    else:
        print('NO')
