def is_palindrome(s):
    s = s.lower()
    r = s[::-1]
    if s == r:
        return True
    else:
        return False
