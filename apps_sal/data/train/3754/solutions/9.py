def prime_product(n):

    def prime(a):
        if a == 2:
            return True
        if a < 2 or a % 2 == 0:
            return False
        return not any((a % x == 0 for x in range(3, int(a ** 0.5) + 1, 2)))
    if n <= 3:
        return 0
    i = n // 2
    while i > 0:
        if prime(n - i) and prime(i):
            return (n - i) * i
        i -= 1
    return 0
