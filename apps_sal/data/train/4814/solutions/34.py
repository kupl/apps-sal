def is_palindrome(s):
    return s.lower() == (''.join(s[::-1])).lower()

