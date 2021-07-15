def is_palindrome(input):
    string = str(input)
    return string.lower() == string.lower()[::-1]
