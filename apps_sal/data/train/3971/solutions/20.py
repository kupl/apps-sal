def tidyNumber(n):
    print(n)
    previous = n % 10
    while n > 0:
        n //= 10
        checking = n % 10
        if previous < checking:
            return False
        previous = checking
    return True
