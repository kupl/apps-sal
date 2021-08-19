def is_palindrome(s):
    s = s.lower()
    if len(s) == 1:
        return True
    if len(s) % 2 != 0:
        return s[0:len(s) // 2 + 1] == s[:len(s) // 2 - 1:-1]
    else:
        return s[:len(s) // 2] == s[:len(s) // 2 - 1:-1]
