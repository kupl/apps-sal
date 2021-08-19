def reverse_letter(string):
    return ''.join((x for x in reversed(string) if x.isalpha()))
