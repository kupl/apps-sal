def is_palindrome(string):
    string = string.lower()
    if string == string[::-1] :
        return True
    else :
        return False
