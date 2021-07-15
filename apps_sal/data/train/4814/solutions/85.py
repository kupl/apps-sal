def is_palindrome(s):
    s = s.casefold()
    s = list(s)
    if s == list(reversed(s)):
        return True
    else:
        return False
