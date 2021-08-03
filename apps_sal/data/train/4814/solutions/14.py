def is_palindrome(s):
    s = s.lower()
    return True if list(s) == list(s)[::-1] else False
