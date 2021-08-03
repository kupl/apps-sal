def is_palindrome(s):
    return s == s[::-1]


def build_palindrome(s):
    for i in range(len(s)):
        x = s + s[:i][::-1]
        if is_palindrome(x):
            return x
        x = s[-i or len(s):][::-1] + s
        if is_palindrome(x):
            return x
