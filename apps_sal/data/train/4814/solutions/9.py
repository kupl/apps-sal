def is_palindrome(s):
    s = s.upper()
    rev = ''.join((x for x in s[::-1]))
    return rev == s
