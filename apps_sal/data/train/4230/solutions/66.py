def reverse_letter(string):
    str = ''.join([x if x.isalpha() else '' for x in string])
    return str[::-1]


