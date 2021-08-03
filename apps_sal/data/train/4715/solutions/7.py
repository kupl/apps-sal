def build_palindrome(s):
    l = len(s)
    left = next(l - i for i in range(l, 0, -1) if s[:i] == s[i - 1::-1])
    right = next(l - i for i in range(l, 0, -1) if s[-i:] == s[:-i - 1:-1] or left == l - i)
    return s[:-left - 1:-1] + s if left <= right else s + s[right - 1::-1]
