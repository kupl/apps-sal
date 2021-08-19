def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    midpoint = len(s) // 2
    if len(s) % 2 == 1:
        return s[:midpoint] == s[midpoint + 1:][::-1]
    return s[:midpoint] == s[midpoint:][::-1]
