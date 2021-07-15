def alternateCase(s):
    result = ''
    if len(s) == 0 or s == ' ':
        return s
    for letter in s:
        if 'a' <= letter <= 'z':
            result += letter.upper()
        elif 'A' <= letter <= 'Z':
            result += letter.lower()
        else:
            result += letter
    return result
