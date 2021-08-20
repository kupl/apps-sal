def is_palindrome(string):
    string = str(string)
    return string[::-1] == str(string)
