def reverse_letter(string):
    return ''.join((c if c.isalpha() else '' for c in string))[::-1]
