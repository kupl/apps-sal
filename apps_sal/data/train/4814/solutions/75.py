def is_palindrome(s):
    emptystring = ''
    x = s.lower()
    for eachletter in x:
        emptystring = eachletter + emptystring
    return emptystring == x

