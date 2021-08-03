def is_palindrome(val):
    s = str(val)
    half_len = len(s) >> 1
    return s[:half_len] == s[::-1][:half_len]
