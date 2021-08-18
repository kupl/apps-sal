def palindrome(n):
    if not isinstance(n, int) or n < 0:
        return "Not valid"
    rev, temp = 0, n
    while temp > 0:
        a = temp % 10
        rev = rev * 10 + a
        temp //= 10
    return rev == n
