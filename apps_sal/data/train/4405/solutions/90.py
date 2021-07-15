def is_palindrome(string):
    m = list(str(string))
    return m == m[::-1]
