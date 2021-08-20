def reverse_letter(string):
    revstr = string[::-1]
    return ''.join([x for x in list(revstr) if x.isalpha()])
