def is_palindrome(string):
    if type(string) == int:
        string = str(string)
    return True if string == string[::-1] else False
