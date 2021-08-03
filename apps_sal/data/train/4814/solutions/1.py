def is_palindrome(s):
    """return True if word "s" is a palindrome"""
    return s.lower() == s[::-1].lower()
