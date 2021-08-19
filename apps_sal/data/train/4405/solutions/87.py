def is_palindrome(string):
    string = str(string)
    if str(string)[::-1] == string:
        return True
    else:
        return False
