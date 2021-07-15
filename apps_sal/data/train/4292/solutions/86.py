def string_clean(s):
    result = ''
    for elem in s:
        if elem not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            result += elem
    return result
