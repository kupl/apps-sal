def build_palindrome(s):
    i = 1
    p = s
    while p != p[::-1]:
        p = s + s[0:i][::-1]
        i += 1
    return p
