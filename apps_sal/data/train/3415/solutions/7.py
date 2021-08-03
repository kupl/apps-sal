def build_palindrome(s):
    if s == s[::-1]:
        return s
    else:
        for i in range(1, len(s)):
            if s + s[:i][::-1] == (s + s[:i][::-1])[::-1]:
                return s + s[:i][::-1]
