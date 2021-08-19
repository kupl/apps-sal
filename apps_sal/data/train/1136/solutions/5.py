for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    ans = 0
    if n % 2 == 0:
        a = n // 2
        ans = a * k
    else:
        a = n // 2 + 1
        ans = a * k
    print(ans)
