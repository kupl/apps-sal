for _ in range(int(input())):
    (n, k) = [int(v) for v in input().split()]
    ans = n // 2 * (k + 2)
    if n % 2 == 0:
        ans = ans
    else:
        ans += 1 + 2 * k
    print(ans)
