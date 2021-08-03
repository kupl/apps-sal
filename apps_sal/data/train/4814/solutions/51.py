def is_palindrome(s):
    return s.lower() == ''.join(list(reversed(s.lower())))
