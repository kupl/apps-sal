def string_clean(s):
    """
    Function will return the cleaned string
    """
    numset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     ns = ''
    for i in s:
        if i in numset:
            s = s.replace(i, '')
    return s
