def reverse_letter(string):
    rev = string[::-1]
    return ''.join([x for x in rev if (x if x.isalpha() else None)])
