def alternateCase(s):
    result = ''
    for letter in s:
        if letter.islower():
            result += letter.upper()
        elif letter.isupper():
            result += letter.lower()
        else:
            result += letter
    return result
