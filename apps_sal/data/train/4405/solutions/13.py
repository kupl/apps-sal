import string
def is_palindrome(string):
    string = str(string)
    string = string.casefold()
    rev = string[::-1]
    
    if string == rev:
        return True
    else:
        return False
