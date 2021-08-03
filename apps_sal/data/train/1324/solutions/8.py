for i in range(int(input())):
    n, k = map(int, input().split())
    root = int(n**0.5)
    min_sum = (k * (k + 1)) // 2

    gcd = -1

    for i in range(1, root + 1):
        if (n % i == 0):
            sum = n // i
            if (sum >= min_sum):
                gcd = max(gcd, i)
            if (i >= min_sum):
                gcd = max(gcd, sum)

    print(gcd)
