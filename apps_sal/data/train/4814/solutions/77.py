def is_palindrome(s):
    s = s.upper()
    return True if s == s[::-1] else False
