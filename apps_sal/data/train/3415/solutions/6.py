build_palindrome=lambda s:next(s+s[:i][::-1]for i in range(len(s)+1)if s[i:]==s[i:][::-1])
