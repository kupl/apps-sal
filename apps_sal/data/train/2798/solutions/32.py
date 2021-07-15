def to_alternating_case(string):
    str2 = ''
    for char in string:
        if char.isalpha():
            if char.islower():
                r = char.upper()
                str2 += r
            else:
                r = char.lower()
                str2 += r
        else:
            str2 += char
    return str2
