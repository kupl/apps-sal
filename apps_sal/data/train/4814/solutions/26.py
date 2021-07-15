def is_palindrome(s):
    return True if s.lower() == "".join(reversed(s.lower())) else False

