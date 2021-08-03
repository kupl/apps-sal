def is_palindrome(string):
    if(list(str(string)) == list(str(string))[::-1]):
        return True
    return False
