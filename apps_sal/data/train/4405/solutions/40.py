def is_palindrome(string):
    r = str(string)
    z = ""
    for v in r:
        z = v + z
    if z == r:
        return(True)
    else:
        return(False)
