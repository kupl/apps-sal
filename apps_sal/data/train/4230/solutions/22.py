def reverse_letter(string):
    return ''.join((c for c in string if c.isalpha()))[::-1]
