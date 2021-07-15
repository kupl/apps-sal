def is_palindrome(string):
    string = str(string)
    emptystring = ''
    for eachletter in string:
        emptystring = eachletter + emptystring
    return emptystring == string
