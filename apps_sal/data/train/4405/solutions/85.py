import string


def is_palindrome(string):
    string = str(string)
    stra = string[::-1]
    if stra == string:
        return True
    return False
