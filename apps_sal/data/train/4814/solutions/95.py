def is_palindrome(str):
    return str.lower() == ''.join(reversed(str.lower()))
