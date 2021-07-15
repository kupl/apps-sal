def is_palindrome(s):
    s_lower = s.lower()
    return s_lower == s_lower[::-1]

