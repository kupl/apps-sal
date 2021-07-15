def is_palindrome(string):
    word = str(string)[::-1]
    return word == str(string)
