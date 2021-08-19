def reverse_letter(string):
    return ''.join((x for x in string[::-1] if x.isalpha()))
