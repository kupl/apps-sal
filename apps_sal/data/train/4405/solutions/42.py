def is_palindrome(string):
    if type(string) == str:
        return string == string[::-1]
    return str(string) == str(string)[::-1]
