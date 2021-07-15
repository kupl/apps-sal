def is_palindrome(string):
    string = str(string) if not isinstance(string, str) else string
    return string == string[::-1]
