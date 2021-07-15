def is_palindrome(string):
    string = str(string)
    return str(string) == str(string[::-1])
