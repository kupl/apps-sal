def is_palindrome(s):
    s = s.lower()
    return s[:len(s)//2] == s[:len(s)-len(s)//2-1:-1]

