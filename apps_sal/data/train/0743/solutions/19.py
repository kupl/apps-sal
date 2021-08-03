for test in range(int(input())):
    n, k = list(map(int, input().split()))
    if k == 1:
        print("NO")
    else:
        a = n // k
        if a % k == 0:
            print('NO')
        else:
            print('YES')
