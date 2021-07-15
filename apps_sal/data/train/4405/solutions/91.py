def is_palindrome(string):
    string = str(string)
    for i in string:
        nonstring = string[::-1]
    if nonstring == string:
        return True
    else:
        return False
