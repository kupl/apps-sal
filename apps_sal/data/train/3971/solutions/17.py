def tidyNumber(n):
    i = n % 10
    n = n // 10
    while n > 0:
        s = n % 10
        print((i, s, n))
        n = n // 10
        if i < s:
            return False
        i = s
    return True
