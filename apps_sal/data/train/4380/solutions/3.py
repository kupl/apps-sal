def remove_chars(s):
    return ''.join(list((i for i in s if i.isalpha() or i.isspace())))
