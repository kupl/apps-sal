def is_palindrome(s):
    try:
        return s==s[::-1]
    except TypeError:
        c=str(s)
        return c==c[::-1]
