def build_palindrome(s, i=0):

    def bp(s):
        a = s + s[:i][::-1]
        if a == a[::-1]:
            return a
    return bp(s) or bp(s[::-1]) or build_palindrome(s, i + 1)
