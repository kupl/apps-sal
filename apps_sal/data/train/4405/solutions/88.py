def is_palindrome(string):
    l = list(str(string))
    return l[:] == l[::-1]
