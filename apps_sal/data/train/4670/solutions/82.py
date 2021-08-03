def string_to_number(s):
    if s[0] == '-':
        startDigitIdx = 1
    else:
        startDigitIdx = 0

    number = 0

    for n in s[startDigitIdx:]:
        number = number * 10 + (ord(n) - ord('0'))

    if s[0] == '-':
        return -number
    else:
        return number
