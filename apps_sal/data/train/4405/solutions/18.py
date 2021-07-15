def is_palindrome(s):
    if not s:
        return True
    s = str(s)
    return is_palindrome(s[1:-1]) if s[0] == s[-1] else False
