def divisors(n):
    ans = set()
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            ans |= {i, n // i}
    return len(ans)
