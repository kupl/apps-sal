def reverse_letter(s):
    return ''.join((l for l in s if l.isalpha()))[::-1]
