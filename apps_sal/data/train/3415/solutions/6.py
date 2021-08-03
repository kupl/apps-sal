def build_palindrome(s): return next(s + s[:i][::-1]for i in range(len(s) + 1)if s[i:] == s[i:][::-1])
