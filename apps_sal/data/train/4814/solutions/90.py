def is_palindrome(s):
    if not s:
        return True
    s = s.lower()
    i = 0
    while i <= len(s) // 2:
        if s[i] != s[-i - 1]:
            return False
        i += 1
    return True
