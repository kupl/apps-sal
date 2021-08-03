def is_palindrome(s):
    s = s.upper()
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True
