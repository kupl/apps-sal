def is_palindrome(string):
    if type(string) == int:
        string = str(string)
        if string[::-1] == string:
            return True
        else:
            return False
    else:
        return string[::-1] == string
