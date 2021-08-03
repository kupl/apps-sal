def is_palindrome(s):
    s = s.lower()
    s1 = s[::-1]
    return s == s1
