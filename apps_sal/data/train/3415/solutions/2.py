def build_palindrome(s):
    return next((f'{s}{s[:i][::-1]}' for i in range(len(s)) if s[i:] == s[i:][::-1]))
