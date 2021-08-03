def is_palindrome(s):
    return (lambda str: str == str[::-1])(s.lower())
