def is_palindrome(string):
    string = str(string)
    return True if string.lower() == string.lower()[::-1] else False
