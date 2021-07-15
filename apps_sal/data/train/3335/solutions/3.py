def vaporcode(s):
    return '  '.join([letter for word in s.upper().split(' ') for letter in word])
