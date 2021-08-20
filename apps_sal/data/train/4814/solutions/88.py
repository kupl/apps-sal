def is_palindrome(s):
    s = s.upper()
    res = ''.join((i for i in s[::-1]))
    return s == res
