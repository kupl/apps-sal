def string_to_number(s):
    number = 0
    if s[0] == '-':
        for n in s[1:]:
            number = number * 10 + (ord(n) - ord('0'))
        return -number
    else:
        for n in s:
            number = number * 10 + (ord(n) - ord('0'))
        return number
