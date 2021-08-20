for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    if n == 0:
        print(k * (k - 1) % 1000000007)
    elif k == 1:
        print(n ** 2 % 1000000007)
    else:
        turn = k // 2
        point = turn + n
        if k % 2 == 0:
            print((point ** 2 - turn) % 1000000007)
        else:
            print((point ** 2 + turn) % 1000000007)
