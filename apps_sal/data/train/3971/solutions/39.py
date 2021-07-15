def tidyNumber(n):
    last_seen = 10
    while n:
        if n % 10 > last_seen:
            return False
        last_seen = n % 10
        n //= 10
    return True
