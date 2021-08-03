def is_palindrome(s):
    s_lowered = s.lower()
    return s_lowered == s_lowered[::-1]
