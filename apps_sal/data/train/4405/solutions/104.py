def is_palindrome(string):
    string = str(string)
    if string[::-1] == string:
        return True
    else:
        return False
    pass
