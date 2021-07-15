def reverse(n):
    rev = 0
    while n:
        rev = rev * 10 + n % 10
        n //= 10
    return rev
