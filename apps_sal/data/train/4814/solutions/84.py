def is_palindrome(s):
    return s.upper() == ''.join(reversed(s.upper()))
