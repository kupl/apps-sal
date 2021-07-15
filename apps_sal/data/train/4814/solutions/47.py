def is_palindrome(s):
    return s.lower() == s.lower()[::-1]
    # returns True if the string reversed is similar to the original thus a palindrome
    # lower() is required to skip over uppercase letters

