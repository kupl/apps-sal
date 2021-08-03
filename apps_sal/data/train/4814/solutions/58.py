def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    if s[0] != s[len(s) - 1]:
        return False
    w = s.strip(s[0])
    return is_palindrome(w)
