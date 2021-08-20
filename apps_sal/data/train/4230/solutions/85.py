def reverse_letter(string):
    return ''.join((i if i.isalpha() else '' for i in string))[::-1]
