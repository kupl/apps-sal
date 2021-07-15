def is_palindrome(s):
    s = list(s)
    for i in range(0, len(s)):
        s[i] = s[i].lower()
    if s == s[::-1]:
        return True
    else:
        return False
