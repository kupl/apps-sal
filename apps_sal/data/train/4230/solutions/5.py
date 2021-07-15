def reverse_letter(s):
    return ''.join(filter(str.isalpha, s))[::-1]
