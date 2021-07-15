def is_palindrome(string):
    a = str(string)
    if a[::-1] == a:
        return True
    else:
        return False
