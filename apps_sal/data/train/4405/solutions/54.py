def is_palindrome(string):
    word = ""
    for i in str(string):
        word = i + word
    return str(string) == word
