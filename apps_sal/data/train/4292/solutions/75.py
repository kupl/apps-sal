import string
digits = string.digits
def string_clean(s):
    emptystring = ''
    for eachletter in s:
        if eachletter in digits:
            continue
        else:
            emptystring = emptystring + eachletter
    return emptystring
    """
    Function will return the cleaned string
    """
    # Your code here

