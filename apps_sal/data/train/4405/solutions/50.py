def is_palindrome(s):
    if isinstance(s, str):
        return s == s[::-1]
    return s == int(str(s)[::-1])
