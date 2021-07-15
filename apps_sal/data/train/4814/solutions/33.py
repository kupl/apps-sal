def is_palindrome(s):
    s = s.lower()
    sb = s[::-1]
    if s == sb:
        return True
    else:
        return False

