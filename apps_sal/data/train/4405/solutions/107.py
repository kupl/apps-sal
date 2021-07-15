def is_palindrome(string):
    string = str(string)
    string = list(string.lower())
    return string == string[::-1]
