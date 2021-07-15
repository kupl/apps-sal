def alternateCase(s):
    res = ''.join([letter.lower() if letter.isupper() else letter.upper() for letter in s])
    return res
