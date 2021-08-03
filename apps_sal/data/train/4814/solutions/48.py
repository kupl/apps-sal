def is_palindrome(string):
    s = string.lower()
    reversed_string = s[::-1]
    return s == reversed_string
