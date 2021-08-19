def reverse_letter(s):
    return ''.join(filter(lambda x: x.isalpha(), s))[::-1]
