def is_palindrome(s):
    s = s.lower()
    rev = s[::-1]
    if s == rev:
        return True
    else:
        return False
