for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if n == 1:
        print(k)
    else:
        if n % 2 == 0:
            p = n // 2
        else:
            p = (n // 2) + 1
        ans = p * k
        print(ans)
