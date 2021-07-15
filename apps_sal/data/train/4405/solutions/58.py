def is_palindrome(string):
    x = str(string)
    return True if x == x[::-1] else False
