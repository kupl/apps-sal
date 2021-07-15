def is_palindrome(s):
    s = s.upper()
    l = len(s)
    for i in range(l):
        if s[i] != s[l - 1 - i]:
            return False
    return True

