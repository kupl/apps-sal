def build_palindrome(s):
    rev = s[::-1]
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            return s + s[:i][::-1]
        if rev[i:] == rev[i:][::-1]:
            return rev[:i] + s
