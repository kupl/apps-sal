def reverse_letter(string):
    return ''.join((c for c in string[-1::-1] if c.isalpha()))
