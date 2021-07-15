def is_palindrome(string):
    return str(string).lower() == str(string).lower()[::-1]
