import string


def alternateCase(s):
    # your code here
    UPPER = string.ascii_uppercase
    LOWER = string.ascii_lowercase

    result = []
    for letter in s:
        if letter in UPPER:
            result.append(letter.lower())
        else:
            result.append(letter.upper())
    return ''.join(result)
