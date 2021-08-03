def build_palindrome(s):
    xs = (s + s[:i][::-1] for i in range(len(s)))
    return next(x for x in xs if x == x[::-1])
