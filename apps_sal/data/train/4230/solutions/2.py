def reverse_letter(string):
    return ''.join(filter(str.isalpha, reversed(string)))
