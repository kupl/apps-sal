def alternateCase(s):
    result = ''
    for i in s:
        if i.isupper():
            result += i.lower()
        elif i.islower():
            result += i.upper()
        else:
            result += ' '
    return result
