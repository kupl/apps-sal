def tidyNumber(n):
    prev = 10
    while n:
        (n, curr) = divmod(n, 10)
        if curr > prev:
            return False
        prev = curr
    return True
