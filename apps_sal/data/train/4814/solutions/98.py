def is_palindrome(s):
    return bool(s[::-1].lower() == s.lower())
