def build_palindrome(s):
    for n in range(len(s), -1, -1):
        if s[:n] == s[:n][::-1]:
            return s[n:][::-1] + s
        if s[-n:] == s[-n:][::-1]:
            return s + s[:-n][::-1]
