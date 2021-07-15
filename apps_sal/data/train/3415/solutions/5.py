def build_palindrome(s):
    for i in range(-len(s) - 1, 0):
        if s.endswith(s[:i:-1]):
            return s + s[i::-1]
