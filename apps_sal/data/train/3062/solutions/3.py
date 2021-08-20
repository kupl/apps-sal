def palindrome(n):
    return 'Not valid' if type(n) != int or n < 0 else str(n) == str(n)[::-1]
