def reverse_letter(string):
    s = ''.join(filter(str.isalpha, string))
    inverse = s[::-1]
    return inverse
